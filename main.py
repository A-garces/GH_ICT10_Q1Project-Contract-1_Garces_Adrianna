from pyscript import display

# Contact page
title_c = 'Contact us'
descri = 'Any comments? We are willing to hear it!'

locate = 'Our Location'
add = '14-8 Onarimachi, Kamakura-shi, Kanagawa 248-0012 Ohayo Restuarant.'
last_up = 'Updated: August 10, 2024'

phcall = 'Phone Numbers'
call = 'Main number: (555) 273-8492 / Mobile number: (555) 648-3201'
last_phup = 'Updated: September 2, 2024'

emailtitle = 'Email Address'
emailaddress = 'Support@ohayores.com'
last_upemail = 'Updated: May 20, 2023'

hour = 'Working hours = 9 am to 2 am'

display (f'{title_c}', target='title')
display (f'{descri}', target='description')

display (f'{locate}', target='location')
display (f'{add}', target='address')
display (f'{last_up}', target='update')

display (f'{phcall}', target='phnumbers')
display (f'{call}', target='phone')
display (f'{last_phup}', target='up')

display (f'{emailtitle}', target='emailadd')
display (f'{emailaddress}', target='emails')
display (f'{last_upemail}', target='upemail')

display (f'{hour}', target='workinghour')