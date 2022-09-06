from common.models import User

for i in range(1,10):
    u=User(email='test'+str(i)+'@email.com')
    u.company='test'+str(i)
    u.set_password(str(i)*4)
    u.name='test'+str(i)
    u.userType='client'
    u.phone='010'+str(i)*8
    u.jobPosition='job'+str(i)
    u.save()