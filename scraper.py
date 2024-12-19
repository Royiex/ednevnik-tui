import requests
from bs4 import BeautifulSoup
import json
import pathlib
import argparse

parser = argparse.ArgumentParser()
session = requests.Session()

parser.add_argument("-f", "--file", type=argparse.FileType('r'), required=False, help="File with Username Line 1, and Password Line 2.")
parser.add_argument("-j", "--json", default=False, action=argparse.BooleanOptionalAction, required=False, help="Output JSON files of data")

args = parser.parse_args()

response = session.get("https://ocjene.skole.hr/login")
soup = BeautifulSoup(response.text, "html.parser")
csrf_token = soup.find("input", {"name": "csrf_token"})["value"]
user = ""
passw = ""

if args.file:
    with args.file as file:
        user = file.readline().strip()
        passw = file.readline().strip()

if not user or not passw:
    user = input("Enter Username: ")
    passw = input("Enter Password: ")

login_data = {
    "username": user,
    "password": passw,
    "csrf_token": csrf_token,
}
headers = {
    "Referer": "https://ocjene.skole.hr/login",
    "Origin": "https://ocjene.skole.hr",
}


def convert():
    soup = BeautifulSoup(course.text, "lxml")
    classes = []
    for li in soup.select("ul.list > li"):
        course_name = li.select_one(".course-info span:nth-of-type(1)").get_text(strip=True)
        teacher_name = li.select_one(".course-info span:nth-of-type(2)").get_text(strip=True).replace("\n", "").replace("\t", "").replace("                     ", " ")

        average_grade_element = li.select_one(".list-average-grade span")
        average_grade = average_grade_element.get_text(strip=True) if average_grade_element else "N/A"

        grade_link = li.find("a")["href"]

        classes.append({
            "course_name": course_name,
            "teacher_name": teacher_name,
            "average_grade": average_grade,
        #    "grade_link": grade_link,
        })

    classes_data = {
        item["course_name"]: {
            "teacher_name": item["teacher_name"],
            "average_grade": item["average_grade"]
        } for item in classes
    }

    school_data = {
		"class": soup.select_one(".class .bold").get_text(strip=True),
		"school_year": soup.select_one(".class-schoolyear").get_text(strip=True),
		"school_name": soup.select_one(".school-name").get_text(strip=True),
		"school_city": soup.select_one(".school-city").get_text(strip=True).strip("; "),
		"classmaster": soup.select(".classmaster span")[1].get_text(strip=True),
		"user": soup.select_one(".user-name").get_text(strip=True),
		"classes:": classes_data
	}

    school_json = json.dumps(school_data, indent=4, ensure_ascii=False)
    classes_json = json.dumps(classes_data, indent=4, ensure_ascii=False)

    if args.json == True:
        pathlib.Path("main.json").write_text(school_json)
        pathlib.Path("classes.json").write_text(classes_json)

    return(school_json)

login_response = session.post("https://ocjene.skole.hr/login", data=login_data, headers=headers)
if login_response.url == "https://ocjene.skole.hr/login":
    raise ValueError("Wrong Username or Passowrd!")

course = session.get("https://ocjene.skole.hr/course")

convert()
