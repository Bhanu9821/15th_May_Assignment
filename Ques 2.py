txt1 = 'Hey, {name} Here!'
txt2 = 'My SID is {SID}'
txt3 = 'I am from {branch} department and my CGPA is {CGPA}'
print(txt1.format(name='Bhanu'), ('\n'), txt2.format(
    SID=21102056), ('\n'), txt3.format(branch='Civil', CGPA=8.8))