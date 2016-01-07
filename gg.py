#-*- coding:utf-8 -*-  
from urllib.request import urlopen
import os
from xml.etree import cElementTree as ET

#author  AlexY
#blog   www.dabu.info
#提取android sdk资源，方便使用迅雷等工具加速下载

split_tag_url = ' |-->downloadUrl :  '



print('system-image    start')

SystemImageUrl = 'http://dl.google.com/android/repository/sys-img/android/'

ns = {'sys_img': 'http://schemas.android.com/sdk/android/sys-img/3'}

root = ET.fromstring(urlopen('http://dl.google.com/android/repository/sys-img/android/sys-img.xml').read()  )

print('================system-image=====================')
for systemImage in root.findall('sys_img:system-image', ns):
	 #print('system-image')
	for revision in systemImage.findall('sys_img:revision', ns):
		print(' |-->revision : ', revision.text)
			
	for description in systemImage.findall('sys_img:description', ns):
		print(' |-->Android SDK Platform : ', description.text)
		
	for api_level in systemImage.findall('sys_img:api-level', ns):
		print(' |-->api level : ', api_level.text)

	for archives in systemImage.findall('sys_img:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('sys_img:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('sys_img:url', ns):
				print(split_tag_url +SystemImageUrl+url.text)
				
				

print( '\n')
print('system-image    end')




print( '\n')
print( '\n')

				


				
				
				
				
print('  Google Apis   system-image     start')
print( '\n')


SystemImageUrl = 'https://dl.google.com/android/repository/sys-img/google_apis/'

ns = {'sys_img': 'http://schemas.android.com/sdk/android/sys-img/3'}

root = ET.fromstring(urlopen('http://dl.google.com/android/repository/sys-img/google_apis/sys-img.xml').read()  )

print('================ system-image=====================')
for systemImage in root.findall('sys_img:system-image', ns):
	 #print('system-image')
	for revision in systemImage.findall('sys_img:revision', ns):
		print(' |-->revision : ', revision.text)
			
	for description in systemImage.findall('sys_img:description', ns):
		print(' |-->Android SDK Platform : ', description.text)
		
	for api_level in systemImage.findall('sys_img:api-level', ns):
		print(' |-->api level : ', api_level.text)

	for archives in systemImage.findall('sys_img:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('sys_img:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('sys_img:url', ns):
				print(split_tag_url +SystemImageUrl+url.text)
				
				

print( '\n')
print('   Google Apis   system-image    end')

print( '\n')



addonUrl = 'https://dl.google.com/android/repository/sys-img/x86/'

ns = {'addon': 'http://schemas.android.com/sdk/android/addon/7'}

root = ET.fromstring(urlopen('http://dl.google.com/android/repository/sys-img/x86/addon-x86.xml').read()  )
#root = ET.fromstring(urlopen('http://45.78.3.206/down/addon.xml').read()  )



print( '\n')

for add_on in root.findall('addon:add-on', ns):
	#print('add-on ')

	for archives in add_on.findall('addon:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('addon:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('addon:url', ns):
				if 'http' in url.text :
					print(url.text)
				else:
					print(addonUrl+ url.text)







				
				
				
				
print( '\n')
print( '\n')

print('repository   start ')
repositoryUrl = 'http://dl.google.com/android/repository/'

ns = {'repository': 'http://schemas.android.com/sdk/android/repository/11'}

root = ET.fromstring(urlopen('https://dl.google.com/android/repository/repository-11.xml').read()  )



print( '\n')

print('================platform=====================')

for platform in root.findall('repository:platform', ns):
	#print('platform')
	for revision in platform.findall('repository:revision', ns):
		strRevison = revision.text
		
			
	for description in platform.findall('repository:description', ns):
		strdescription = description.text
		
		
	for api_level in platform.findall('repository:api-level', ns):
		strapi_level = api_level.text
		

	for archives in platform.findall('repository:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('repository:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('repository:url', ns):
				if 'linux' in url.text:
					print('')
				elif 'macosx' in url.text:
					print('')
				else:
					print(' |-->revision : ', strRevison)
					print(' |-->Android SDK Platform : ', strdescription)
					print(' |-->api level : ', strapi_level)
					if 'http' in url.text :
						print(split_tag_url +url.text)
					else:
						print(split_tag_url +repositoryUrl+ url.text)
				
				

print('\n')

print('================sample=====================')

for sample in root.findall('repository:sample', ns):
	#print('sample')
	for revision in sample.findall('repository:revision', ns):
		print(' |-->revision : ', revision.text)
			
		
	for api_level in platform.findall('repository:api-level', ns):
		print(' |-->api level : ', api_level.text)

	for archives in platform.findall('repository:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('repository:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('repository:url', ns):
				if 'http' in url.text :
					print(split_tag_url +url.text)
				else:
					print(split_tag_url +repositoryUrl+ url.text)
					
					
					

print( '\n')

print('================platform-tool=====================')

for platform_tool in root.findall('repository:platform-tool', ns):
	#print('platform_tool')

	for archives in platform_tool.findall('repository:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('repository:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('repository:url', ns):
				if 'windows' in url.text :
					print(repositoryUrl+ url.text)
					
				

print( '\n')

print('================build-tool=====================')

for build_tool in root.findall('repository:build-tool', ns):
	#print('build_tool ')

	for archives in build_tool.findall('repository:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('repository:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('repository:url', ns):
				if 'windows' in url.text :
					if 'http' in url.text :
						print(url.text)
					else:
						print(repositoryUrl+ url.text)
						

print( '\n')

print('================tools=====================')

for tool in root.findall('repository:tool', ns):
	#print('tool ')

	for archives in tool.findall('repository:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('repository:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('repository:url', ns):
				if 'windows' in url.text :
					if 'http' in url.text :
						print(url.text)
					else:
						print(repositoryUrl+ url.text)
						
						
						
						

print( '\n')

print('================doc=====================')

for doc in root.findall('repository:doc', ns):
	#print('doc ')

	for archives in doc.findall('repository:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('repository:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('repository:url', ns):
					print(repositoryUrl+ url.text)
					
					
					

print( '\n')

print('================source=====================')

for source in root.findall('repository:source', ns):
	#print('source ')

	for archives in source.findall('repository:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('repository:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('repository:url', ns):
				if 'http' in url.text :
					print( url.text)
				else:
					print(repositoryUrl+ url.text)
					
					

print( '\n')

print('repository   end ')



print( '\n')


print('add-on  start ')
addonUrl = 'https://dl.google.com/android/repository/'

ns = {'addon': 'http://schemas.android.com/sdk/android/addon/7'}

root = ET.fromstring(urlopen('http://dl.google.com/android/repository/addon.xml').read()  )
#root = ET.fromstring(urlopen('http://45.78.3.206/down/addon.xml').read()  )





print('================add-on=====================')
print( '\n')

for add_on in root.findall('addon:add-on', ns):
	#print('add-on ')

	for archives in add_on.findall('addon:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('addon:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('addon:url', ns):
				if 'http' in url.text :
					print(url.text)
				else:
					print(addonUrl+ url.text)



print( '\n')




print('================extra=====================')
print( '\n')

for extra in root.findall('addon:extra', ns):
	#print('add-on ')

	for archives in extra.findall('addon:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('addon:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('addon:url', ns):
				if 'http' in url.text :
					print(url.text)
				else:
					print(addonUrl+ url.text)

					
					
print('add-on end')



print( '\n')



######################################################
print('================Android Support Library=====================')
print( '\n')

addonUrl = 'https://dl.google.com/android/repository/'

ns = {'addon': 'http://schemas.android.com/sdk/android/addon/6'}

root = ET.fromstring(urlopen('https://dl.google.com/android/repository/addon-6.xml').read()  )


for extra in root.findall('addon:extra', ns):
	#print('add-on ')

	for archives in extra.findall('addon:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('addon:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('addon:url', ns):
				if 'http' in url.text :
					print(url.text)
				else:
					print(addonUrl+ url.text)

					
					


print( '\n')



print('Intel x86 Emulator Accelerator (HAXM installer)     start')

addonUrl = 'https://dl.google.com/android/repository/'

ns = {'addon': 'http://schemas.android.com/sdk/android/addon/7'}

root = ET.fromstring(urlopen('https://dl.google.com/android/repository/extras/intel/addon.xml').read()  )
#root = ET.fromstring(urlopen('http://45.78.3.206/down/addon.xml').read()  )

print( '\n')

for extra in root.findall('addon:extra', ns):
	#print('add-on ')

	for archives in extra.findall('addon:archives', ns):
		#print(' |-->', archives.text)
		for archive in archives.findall('addon:archive', ns):
			#print(' |-->', archive.text)
			for url in archive.findall('addon:url', ns):
				if 'windows' in url.text :
					print(addonUrl+url.text)




print( '\n')
print('Intel x86 Emulator Accelerator (HAXM installer)    end')



