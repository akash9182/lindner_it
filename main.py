# import urllib.request
# curl -s "https://ucprod.service-now.com/api/now/table/cmdb_ci_computer?x_loaner_depot=Lindner%20College%20of%20Business&x_loaner_isloaner=true&u_loaner_status=Checked%20out" --request GET --header "Accept:application/json" --user "scriptuser":"" | jq '.' | grep -c asset_tag 


import shlex
import subprocess
from lxml import etree 

cmd = '''curl -s "https://ucprod.service-now.com/api/now/table/cmdb_ci_computer?x_loaner_depot=Lindner%20College%20of%20Business&x_loaner_isloaner=true&u_loaner_status=Checked%20out" --request GET --header "Accept:application/json" --user "ranaas1":"#Nevergiveup1" | jq '.' | grep -c asset_tag '''
args = shlex.split(cmd)
process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print(type(stdout))
# print(stdout)


doc = etree.parse(stdout)
root = doc.getroot()

result = len(root.xpath("//asset_path"))

print(result)