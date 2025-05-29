#### using [] to create a list

names : list = ['John', 'Jane', 'Doe', 'Smith', 'Alice']
names[5] = 'Bob'
names[2] = 'Charlie'
print(names)

###Using list constructor to create a list
apps : list = list()
apps.append('Facebook')
apps.append('Instagram')
apps.append('Twitter')
apps.append('Snapchat')
apps.append('Linkedin')
apps.append('Whatsapp')
apps.append('Tiktok')
apps.append('YouTube')
new_apps = apps.copy()
print(new_apps)
print(apps.count('Facebook'))
apps.extend(['Pinterest', 'Reddit', 'Tumblr'])
apps.insert(2, 'Flickr')
apps.remove('Facebook')
the_app = apps.pop(3)
print(the_app.upper())
apps.reverse()
apps.sort(reverse=True)
apps.clear()

print(apps)