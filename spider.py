import scraperwiki
import lxml.html
import csv

html = scraperwiki.scrape("http://bbmpelections.in/wards")
root = lxml.html.fromstring(html)
wards = open("wards.csv", 'a')
data = {"ward_no": '', "ward_name": '', "category": '', "representative": '', "population": '', "male": '',
"female": '', "sc": '', "st": '', "area": '', "constituency": '', "localities": []}

csv_writer = csv.DictWriter(wards, fieldnames=data.keys(), dialect='excel')
csv_writer.writeheader()

for tr in root.cssselect("table[class='listing'] tr"):
    row = tr.cssselect("td")
    if row!= []:
        data["ward_no"] = row[0].text_content()
        data["ward_name"] = row[1].text_content()
        data["category"] = row[2].text_content()
        data["representative"] = row[3].text_content()
        ward_html = scraperwiki.scrape("http://bbmpelections.in/wards/"+data["ward_no"])
        ward_root = lxml.html.fromstring(ward_html)
        ward_tr = ward_root.cssselect("table[class='info'] tr")
        data["population"] = ward_tr[2].cssselect("td")[0].text_content()
        data["male"] = ward_tr[3].cssselect("td")[0].text_content()
        data["female"] = ward_tr[4].cssselect("td")[0].text_content()
        data["sc"] = ward_tr[5].cssselect("td")[0].text_content()
        data["st"] = ward_tr[6].cssselect("td")[0].text_content()
        data["area"] = ward_tr[7].cssselect("td")[0].text_content()
        data["constituency"] = ward_tr[8].cssselect("td")[0].text_content()
        data["localities"] = ward_tr[9].cssselect("td")[0].text_content().split(',')
        print data
        csv_writer.writerow(data)
