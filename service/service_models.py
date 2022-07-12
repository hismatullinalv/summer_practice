from service.models import Sessions, Dep, Vendors, License, PC, User
from datetime import datetime


class Services_models:
    _objects = {}
    _lines = []

    @classmethod
    def update_db(cls):
        with open('/Users/owner/PycharmProjects/djangoProject/service/file.txt', 'r') as inf, open(
                '/Users/owner/PycharmProjects/djangoProject/service/outfile.txt', 'w') as out:
            for line in inf:
                if line.strip():
                    out.write(line)
        out = open('/Users/owner/PycharmProjects/djangoProject/service/outfile.txt', 'r')
        lines = out.readlines()
        server_line = []
        for index_, line in enumerate(lines):
            if line.startswith('  "'):
                end = line.rfind('"')
                start = line.find('vendor: ') + 8
                if not Vendors.objects.filter(name_vendor=line[start:]).exists():
                    vendor = Vendors()
                    vendor.name_vendor = line[start:]
                    vendor.save()

                if not License.objects.filter(name_lic=line[3:end],
                                              vendor_id=Vendors.objects.get(name_vendor=line[start:])):
                    license = License()
                    license.name_lic = line[3:end]
                    license.vendor_id = Vendors.objects.get(name_vendor=line[start:])
                    license.save()

                line_lic = lines[index_ - 1]
                num_lic_s = line_lic.find(';  Total of') + 12
                num_lic_e = line_lic.find('in use') - 9
                num_lic1 = line_lic[num_lic_s:num_lic_e]

                ind = index_ + 2
                flag = True
                while flag:
                    if lines[ind].find('Users') == -1:
                        line_session = lines[ind].replace(',', '').split()
                        if not Dep.objects.filter(num_dep=line_session[0][0:4]).exists():
                            dep = Dep()
                            dep.num_dep = line_session[0][0:4]
                            dep.save()

                        if not User.objects.filter(name_user=line_session[0][5:],
                                                   dep_id=Dep.objects.get(num_dep=line_session[0][0:4])).exists():
                            user = User()
                            user.name_user = line_session[0][5:]
                            user.dep_id = Dep.objects.get(num_dep=line_session[0][0:4])
                            user.save()

                        if not PC.objects.filter(num_pc=line_session[1]).exists():
                            pc = PC()
                            pc.num_pc = line_session[1]
                            pc.save()

                        date_string = line_session[8] + line_session[9] + line_session[10] + '2022'
                        date_format = datetime.strptime(date_string, "%a%d/%m%H:%M%Y")

                        if not Sessions.objects.filter(user_id=User.objects.get(name_user=line_session[0][5:],
                                                                                dep_id=Dep.objects.get(
                                                                                    num_dep=line_session[0][0:4])),
                                                       pc_id=PC.objects.get(num_pc=line_session[1]),
                                                       date_start=date_format,
                                                       lic_id=License.objects.get(name_lic=line[3:end])).exists():
                            session = Sessions()
                            session.user_id = User.objects.get(name_user=line_session[0][5:],
                                                               dep_id=Dep.objects.get(num_dep=line_session[0][0:4]))

                            if len(num_lic1) >= 3:

                                session.num_lic = line_session[11]
                            else:
                                session.num_lic = 1
                            session.lic_id = License.objects.get(name_lic=line[3:end])
                            session.date_start = date_format
                            session.pc_id = PC.objects.get(num_pc=line_session[1])
                            session.save()

                        if len(num_lic1) >= 3:
                            num_lic = line_session[11]
                        else:
                            num_lic = 1

                        log_line = {'license': License.objects.get(name_lic=line[3:end]),
                                    'start': date_format,
                                    'user': User.objects.get(name_user=line_session[0][5:],
                                                             dep_id=Dep.objects.get(
                                                                 num_dep=line_session[0][0:4])),
                                    'amount': num_lic,
                                    'pc': PC.objects.get(num_pc=line_session[1]),
                                    'vendor': Vendors.objects.get(name_vendor=line[start:]),
                                    }
                        server_line.append(log_line)

                        ind += 1

                    else:
                        flag = False
        cls._objects = server_line

    def create_objects(self):
        self.update_db()

    @classmethod
    def get_objects(cls):
        return cls._objects
