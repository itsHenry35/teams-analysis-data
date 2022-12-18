import requests
def teams_fetch_attendance_by_link(link):
    client_id = "0a24fa7b-5cf3-440b-a85e-63b8e1f09f67"
    client_secrets = "xHU8Q~4FvGzI_ghpaz8R17wSx4-gphkgmRI5rb4o"
    endpoint = "https://login.microsoftonline.com/b9fa471e-392b-4c4a-89bd-933bbccf8c91/oauth2/v2.0/token"
    token = requests.post(endpoint, data={
        "client_id": client_id,
        "client_secret": client_secrets,
        "grant_type": "client_credentials",
        "scope": "https://graph.microsoft.com/.default"
    }).json()["access_token"]
    url = "https://graph.microsoft.com/beta/users/c1076175-1702-4c13-873f-4045571dcc87/onlineMeetings?$filter=JoinWebUrl%20eq%20'" + link +"'"
    headers = {
        "Authorization": "Bearer " + token
    }
    meetingid = requests.get(url, headers=headers).json()['value'][0]['id']
    url = "https://graph.microsoft.com/beta/users/c1076175-1702-4c13-873f-4045571dcc87/onlineMeetings/" + meetingid + "/attendanceReports"
    reportids = requests.get(url, headers=headers)
    result = reportids.json()['value']
    reportid = result[len(result)-1]['id']
    url = "https://graph.microsoft.com/beta/users/c1076175-1702-4c13-873f-4045571dcc87/onlineMeetings/" + meetingid + "/attendanceReports/" + reportid + "/attendanceRecords"
    report = requests.get(url, headers=headers)
    return report.json()

if __name__ == '__main__':
    result = teams_fetch_attendance_by_link("https://teams.microsoft.com/l/meetup-join/19:meeting_NGIxOWIyMzUtZjViNi00ZDVkLWJhYTItMTBhZTc2M2M1MzNi@thread.v2/0?context=%7B%22Tid%22:%22b9fa471e-392b-4c4a-89bd-933bbccf8c91%22,%22Oid%22:%22c1076175-1702-4c13-873f-4045571dcc87%22%7D")
    fileobj = open("result.json", "w", encoding="utf-16")
    fileobj.write(str(result))
    fileobj.close()