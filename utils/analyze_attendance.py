from datetime import datetime, timedelta
from dateutil import parser

def process_time(seconds):
    h = seconds//3600
    m = seconds//60%60
    s = seconds%60
    return f"""{h}小时 {m}分钟 {s}秒"""

def process_time2(time):
    _date = parser.parse(time)
    local_time = _date + timedelta(hours=8)
    end_time = local_time.strftime("%H:%M:%S")
    return end_time

def get_attendance_by_json(json):
    names = [
        {
            "name": "叶陈果", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "胡雯宁", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "王琪琦", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "陈静奕", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "赵慧钦", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "钟佳琪", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "郭婧萱", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "黄昕妍", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "杨羽瑶", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "俞孙湉", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "丁许洲", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "俞玟溪", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "陆佳琳", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "方子欣", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "黄新蕊", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "郭子涵", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "徐悦", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "张玥尧", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "李禹璇", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "苗羽涵", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "李晨萱", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "赵翎菟", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "柯圣劼", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "柏天", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "朱恒睿", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "祝张章", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "黄煜宸", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "李雨轩", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "王浩", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "侯飞", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "高家宜", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "李鸿基", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "刘卿睿", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "韩承希", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "张羿翔", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "费丞譞", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "徐朱乐", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "张嘉誉", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "庄贝奇", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "许文达", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "王者", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "朱叶青", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "侯昱炜", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "张睿辰", 
            "inmeetingtime": 0, 
            "jointime": 0
        }, 
        {
            "name": "李凯文", 
            "inmeetingtime": 0, 
            "jointime": 0
        }
    ]

    unknownperson = []

    json = json['value']
    for i in json:
        unknown = 1
        for a in names:
            if a['name'] in i['identity']['displayName']:
                if a['jointime'] == 0:
                    a['jointime'] = i['attendanceIntervals'][0]['joinDateTime']
                a['inmeetingtime'] += i['attendanceIntervals'][0]['durationInSeconds']
                unknown = 0
        if unknown == 1:
            unknownperson.append({
                "name": i['identity']['displayName'],
                "inmeetingtime": i['attendanceIntervals'][0]['durationInSeconds'],
                "jointime": i['attendanceIntervals'][0]['joinDateTime'],
            })
    names.sort(key=lambda x: x['inmeetingtime'], reverse=False)
    meetingtimeinsec = names[len(names)-1]['inmeetingtime']
    meetingtime = process_time(meetingtimeinsec)
    meetingstart = process_time2(names[len(names)-1]['jointime'])
    attended = ""
    unknownattended = ""
    for i in names:
        time = process_time(i['inmeetingtime'])
        time2 = process_time2(i['jointime'])
        attended += "名称：" + i['name'] + " 加入课堂时间：" + time2 + ' 参与课堂时长：' + time + '<br />'

    for i in unknownperson:
        time = process_time(i['inmeetingtime'])
        time2 = process_time2(i['jointime'])
        unknownattended += "名称：" + i['name'] + " 加入课堂时间：" + time2 + ' 参与课堂时长：' + time + '<br />'

    result = f"""
    会议时长：{meetingtime}<br />
    会议开始时间：{meetingstart}<br /><br />
    会议参与人员：<br />{attended}<br />
    未知人员：<br />{unknownattended}
    """

    return result
    

if __name__ == '__main__':
    json = {'@odata.context': "https://graph.microsoft.com/beta/$metadata#users('c1076175-1702-4c13-873f-4045571dcc87')/onlineMeetings('MSpjMTA3NjE3NS0xNzAyLTRjMTMtODczZi00MDQ1NTcxZGNjODcqMCoqMTk6bWVldGluZ19OR0l4T1dJeU16VXRaalZpTmkwMFpEVmtMV0poWVRJdE1UQmhaVGMyTTJNMU16TmlAdGhyZWFkLnYy')/attendanceReports('b64e70f9-6a93-4edd-b8ad-98e839affe39')/attendanceRecords", 'value': [{'id': 'c1076175-1702-4c13-873f-4045571dcc87', 'emailAddress': 'zhr0305@itshenry.ml', 'totalAttendanceInSeconds': 3283, 'role': 'Organizer', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'c1076175-1702-4c13-873f-4045571dcc87', 'displayName': '朱恒睿', 'tenantId': 'b9fa471e-392b-4c4a-89bd-933bbccf8c91'}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:00:15.2457389Z', 'leaveDateTime': '2022-12-16T01:54:58.9688692Z', 'durationInSeconds': 3283}]}, {'id': 'df544cde-2b64-4be1-a165-4fa5108fb132', 'emailAddress': '', 'totalAttendanceInSeconds': 186, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'df544cde-2b64-4be1-a165-4fa5108fb132', 'displayName': '陈静奕  (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:01:25.601889Z', 'leaveDateTime': '2022-12-16T01:04:32.4937462Z', 'durationInSeconds': 186}]}, {'id': '23ab837e-dcc6-44be-a943-e334edb68684', 'emailAddress': '', 'totalAttendanceInSeconds': 21, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '23ab837e-dcc6-44be-a943-e334edb68684', 'displayName': '. (Guest)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:02:37.9197727Z', 'leaveDateTime': '2022-12-16T01:02:59.6646869Z', 'durationInSeconds': 21}]}, {'id': '30f00913-a34c-456d-9552-201864128195', 'emailAddress': '', 'totalAttendanceInSeconds': 2819, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '30f00913-a34c-456d-9552-201864128195', 'displayName': '苗羽涵 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:03:59.948946Z', 'leaveDateTime': '2022-12-16T01:50:59.7157347Z', 'durationInSeconds': 2819}]}, {'id': '9f7db7fc-f471-4072-8adb-b39f51d46901', 'emailAddress': '', 'totalAttendanceInSeconds': 2803, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '9f7db7fc-f471-4072-8adb-b39f51d46901', 'displayName': '张玥尧 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:03.5662274Z', 'leaveDateTime': '2022-12-16T01:50:46.6382633Z', 'durationInSeconds': 2803}]}, {'id': 'a5cbb91b-e32f-41f1-9273-1e8e1db7c3bd', 'emailAddress': '', 'totalAttendanceInSeconds': 2798, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'a5cbb91b-e32f-41f1-9273-1e8e1db7c3bd', 'displayName': '黄煜宸', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:05.4727701Z', 'leaveDateTime': '2022-12-16T01:50:43.9258981Z', 'durationInSeconds': 2798}]}, {'id': '7965e954-b132-461f-8cfa-d4643beb3962', 'emailAddress': '', 'totalAttendanceInSeconds': 2792, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '7965e954-b132-461f-8cfa-d4643beb3962', 'displayName': '李雨轩  36号  （主讲人） (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:14.5676238Z', 'leaveDateTime': '2022-12-16T01:50:46.7145663Z', 'durationInSeconds': 2792}]}, {'id': '072177bf-c545-471f-8bcd-50490c1630ff', 'emailAddress': '', 'totalAttendanceInSeconds': 2785, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '072177bf-c545-471f-8bcd-50490c1630ff', 'displayName': '侯飞', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:17.0215421Z', 'leaveDateTime': '2022-12-16T01:50:42.7488829Z', 'durationInSeconds': 2785}]}, {'id': 'f140702d-a1de-44fe-8fe3-b69603e8cbcd', 'emailAddress': '', 'totalAttendanceInSeconds': 2783, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'f140702d-a1de-44fe-8fe3-b69603e8cbcd', 'displayName': '庄贝奇 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:17.2111031Z', 'leaveDateTime': '2022-12-16T01:50:40.5593454Z', 'durationInSeconds': 2783}]}, {'id': '91047d19-2acf-4323-8cc4-dd2b8ad6968a', 'emailAddress': '', 'totalAttendanceInSeconds': 2788, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '91047d19-2acf-4323-8cc4-dd2b8ad6968a', 'displayName': '丁许洲 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:17.6484527Z', 'leaveDateTime': '2022-12-16T01:50:45.7439018Z', 'durationInSeconds': 2788}]}, {'id': '2b9af89b-4203-4b6c-a922-6d34c0e8948b', 'emailAddress': '', 'totalAttendanceInSeconds': 2796, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '2b9af89b-4203-4b6c-a922-6d34c0e8948b', 'displayName': '刘卿睿', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:17.9415299Z', 'leaveDateTime': '2022-12-16T01:50:54.6893058Z', 'durationInSeconds': 2796}]}, {'id': 'c932d648-9012-48be-a543-b5436ebabfc8', 'emailAddress': '', 'totalAttendanceInSeconds': 2794, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'c932d648-9012-48be-a543-b5436ebabfc8', 'displayName': '陈静奕   (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:20.3127315Z', 'leaveDateTime': '2022-12-16T01:50:54.9926198Z', 'durationInSeconds': 2794}]}, {'id': '774cb51b-1ebe-4391-bf94-d88f6b1d94d3', 'emailAddress': '', 'totalAttendanceInSeconds': 2814, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '774cb51b-1ebe-4391-bf94-d88f6b1d94d3', 'displayName': '徐悦（贵宾小姐）  (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:21.6359252Z', 'leaveDateTime': '2022-12-16T01:51:16.0949714Z', 'durationInSeconds': 2814}]}, {'id': '0f5e35a0-8b2c-4aee-b57d-8214ca7363d6', 'emailAddress': '', 'totalAttendanceInSeconds': 1690, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '0f5e35a0-8b2c-4aee-b57d-8214ca7363d6', 'displayName': '俞玟溪 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:22.6517677Z', 'leaveDateTime': '2022-12-16T01:32:33.1233162Z', 'durationInSeconds': 1690}]}, {'id': '266b5137-713e-469f-b69f-03a2388f8fdd', 'emailAddress': '', 'totalAttendanceInSeconds': 156, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '266b5137-713e-469f-b69f-03a2388f8fdd', 'displayName': '叶陈果 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:25.7805574Z', 'leaveDateTime': '2022-12-16T01:07:02.3940248Z', 'durationInSeconds': 156}]}, {'id': '26fc5eb7-14c2-4b8e-9427-36f70c1fcbea', 'emailAddress': '', 'totalAttendanceInSeconds': 2601, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '26fc5eb7-14c2-4b8e-9427-36f70c1fcbea', 'displayName': '王浩37', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:29.6232196Z', 'leaveDateTime': '2022-12-16T01:47:50.7637515Z', 'durationInSeconds': 2601}]}, {'id': '928a05bd-2a18-45fa-9fed-4bf9d226eb92', 'emailAddress': '', 'totalAttendanceInSeconds': 2782, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '928a05bd-2a18-45fa-9fed-4bf9d226eb92', 'displayName': '张羿翔 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:29.8922022Z', 'leaveDateTime': '2022-12-16T01:50:52.8058146Z', 'durationInSeconds': 2782}]}, {'id': '7883ccf6-c053-4444-8a73-f4962076a2d7', 'emailAddress': '', 'totalAttendanceInSeconds': 2772, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '7883ccf6-c053-4444-8a73-f4962076a2d7', 'displayName': '黄新蕊', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:32.3601283Z', 'leaveDateTime': '2022-12-16T01:50:45.2494364Z', 'durationInSeconds': 2772}]}, {'id': '4b714bdb-368e-4d2a-b886-3556bf4387e7', 'emailAddress': '', 'totalAttendanceInSeconds': 2767, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '4b714bdb-368e-4d2a-b886-3556bf4387e7', 'displayName': '钟佳琪 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:36.3721874Z', 'leaveDateTime': '2022-12-16T01:50:43.8240538Z', 'durationInSeconds': 2767}]}, {'id': '51e92420-6d8a-401a-ad1a-df32fa970e00', 'emailAddress': '', 'totalAttendanceInSeconds': 2780, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '51e92420-6d8a-401a-ad1a-df32fa970e00', 'displayName': '朱叶青', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:37.971452Z', 'leaveDateTime': '2022-12-16T01:50:58.3188023Z', 'durationInSeconds': 2780}]}, {'id': '6acafb88-b344-436c-8841-bd914b0f41f2', 'emailAddress': '', 'totalAttendanceInSeconds': 2765, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '6acafb88-b344-436c-8841-bd914b0f41f2', 'displayName': '李晨萱', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:39.3456903Z', 'leaveDateTime': '2022-12-16T01:50:44.6349452Z', 'durationInSeconds': 2765}]}, {'id': 'ab88fb0b-6a94-48ff-9efd-d08bcc01419d', 'emailAddress': '', 'totalAttendanceInSeconds': 298, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'ab88fb0b-6a94-48ff-9efd-d08bcc01419d', 'displayName': '李鸿基 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:41.007781Z', 'leaveDateTime': '2022-12-16T01:09:39.487624Z', 'durationInSeconds': 298}]}, {'id': '170a6428-762b-4ba4-8998-2e0eea7169ce', 'emailAddress': '', 'totalAttendanceInSeconds': 2764, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '170a6428-762b-4ba4-8998-2e0eea7169ce', 'displayName': '张睿辰', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:41.0968294Z', 'leaveDateTime': '2022-12-16T01:50:45.6507659Z', 'durationInSeconds': 2764}]}, {'id': '9f86c8fc-aa24-4d00-91bc-cfe8b13275e6', 'emailAddress': '', 'totalAttendanceInSeconds': 2771, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '9f86c8fc-aa24-4d00-91bc-cfe8b13275e6', 'displayName': '杨羽瑶 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:42.6159474Z', 'leaveDateTime': '2022-12-16T01:50:53.7122379Z', 'durationInSeconds': 2771}]}, {'id': '273866c7-54b5-4b9c-bb4c-5b95446bd0ff', 'emailAddress': '', 'totalAttendanceInSeconds': 2791, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '273866c7-54b5-4b9c-bb4c-5b95446bd0ff', 'displayName': '俞孙湉 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:46.6285798Z', 'leaveDateTime': '2022-12-16T01:51:18.0461265Z', 'durationInSeconds': 2791}]}, {'id': '5a54bb78-ba27-4957-b10b-b730a5f20836', 'emailAddress': '', 'totalAttendanceInSeconds': 2779, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '5a54bb78-ba27-4957-b10b-b730a5f20836', 'displayName': '韩承希 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:48.8069633Z', 'leaveDateTime': '2022-12-16T01:51:08.7220836Z', 'durationInSeconds': 2779}]}, {'id': '62fa9d1b-578c-446b-b0b6-3dc893f6ba6c', 'emailAddress': '', 'totalAttendanceInSeconds': 2758, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '62fa9d1b-578c-446b-b0b6-3dc893f6ba6c', 'displayName': '郭子涵 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:51.4021646Z', 'leaveDateTime': '2022-12-16T01:50:49.6557406Z', 'durationInSeconds': 2758}]}, {'id': 'dc44daa4-4d75-48ec-90a7-2684e6138a3c', 'emailAddress': '', 'totalAttendanceInSeconds': 2754, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'dc44daa4-4d75-48ec-90a7-2684e6138a3c', 'displayName': '王琪琦 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:52.0363165Z', 'leaveDateTime': '2022-12-16T01:50:46.5438118Z', 'durationInSeconds': 2754}]}, {'id': '5d8453a7-7974-4a7a-b447-3c4cde58418c', 'emailAddress': '', 'totalAttendanceInSeconds': 2307, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '5d8453a7-7974-4a7a-b447-3c4cde58418c', 'displayName': '陆佳琳 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:04:52.5948313Z', 'leaveDateTime': '2022-12-16T01:43:20.4327195Z', 'durationInSeconds': 2307}]}, {'id': 'b8fae294-0942-4a82-bcea-7ade59608d03', 'emailAddress': '', 'totalAttendanceInSeconds': 2757, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'b8fae294-0942-4a82-bcea-7ade59608d03', 'displayName': '赵慧钦', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:05:02.6440902Z', 'leaveDateTime': '2022-12-16T01:51:00.5673796Z', 'durationInSeconds': 2757}]}, {'id': '473a5514-6eb1-48f5-b893-ccdacf887e71', 'emailAddress': '', 'totalAttendanceInSeconds': 2738, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '473a5514-6eb1-48f5-b893-ccdacf887e71', 'displayName': '赵翎菟22', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:05:07.3824556Z', 'leaveDateTime': '2022-12-16T01:50:46.356276Z', 'durationInSeconds': 2738}]}, {'id': '2101417a-6b07-4f3d-8e2b-82c735587880', 'emailAddress': '', 'totalAttendanceInSeconds': 2752, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '2101417a-6b07-4f3d-8e2b-82c735587880', 'displayName': '张嘉誉', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:05:24.6012235Z', 'leaveDateTime': '2022-12-16T01:51:17.077753Z', 'durationInSeconds': 2752}]}, {'id': '31f2ad23-6cbb-4cb8-b595-87749ce41c4d', 'emailAddress': '', 'totalAttendanceInSeconds': 161, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '31f2ad23-6cbb-4cb8-b595-87749ce41c4d', 'displayName': '胡雯宁 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:05:26.1787803Z', 'leaveDateTime': '2022-12-16T01:08:07.922613Z', 'durationInSeconds': 161}]}, {'id': 'ae8f2dba-0043-4b85-9037-f265ab1d20a5', 'emailAddress': '', 'totalAttendanceInSeconds': 2744, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'ae8f2dba-0043-4b85-9037-f265ab1d20a5', 'displayName': '祝张章 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:05:27.3984514Z', 'leaveDateTime': '2022-12-16T01:51:12.0207344Z', 'durationInSeconds': 2744}]}, {'id': '0a77473c-132b-46d0-9f53-49faff897ce2', 'emailAddress': '', 'totalAttendanceInSeconds': 2721, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '0a77473c-132b-46d0-9f53-49faff897ce2', 'displayName': '黄昕妍   (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:05:29.2755428Z', 'leaveDateTime': '2022-12-16T01:50:50.7799672Z', 'durationInSeconds': 2721}]}, {'id': 'dc2699cb-74f6-4675-98ba-41b063fc6519', 'emailAddress': '', 'totalAttendanceInSeconds': 2718, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'dc2699cb-74f6-4675-98ba-41b063fc6519', 'displayName': '许文达 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:05:34.2762073Z', 'leaveDateTime': '2022-12-16T01:50:52.3718425Z', 'durationInSeconds': 2718}]}, {'id': 'f40b3f7c-801b-400e-9900-4afeb3cea07c', 'emailAddress': '', 'totalAttendanceInSeconds': 2682, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'f40b3f7c-801b-400e-9900-4afeb3cea07c', 'displayName': '侯昱炜 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:06:02.0948208Z', 'leaveDateTime': '2022-12-16T01:50:44.4682652Z', 'durationInSeconds': 2682}]}, {'id': '39d9324a-199e-494d-b873-f7521c1c8989', 'emailAddress': '', 'totalAttendanceInSeconds': 2693, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '39d9324a-199e-494d-b873-f7521c1c8989', 'displayName': '方子欣  （VIP) (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:06:21.9727731Z', 'leaveDateTime': '2022-12-16T01:51:15.0311731Z', 'durationInSeconds': 2693}]}, {'id': '5976434c-885f-45ff-b10a-76b2652ed579', 'emailAddress': '', 'totalAttendanceInSeconds': 2603, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '5976434c-885f-45ff-b10a-76b2652ed579', 'displayName': '徐朱乐', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:07:19.9597321Z', 'leaveDateTime': '2022-12-16T01:50:43.0612767Z', 'durationInSeconds': 2603}]}, {'id': '2be021af-8602-4707-b9e4-10d920f5a567', 'emailAddress': '', 'totalAttendanceInSeconds': 1090, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '2be021af-8602-4707-b9e4-10d920f5a567', 'displayName': '高家宜 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:07:25.8539456Z', 'leaveDateTime': '2022-12-16T01:25:35.8699843Z', 'durationInSeconds': 1090}]}, {'id': '61a109a3-7049-4a35-9e24-e816f08ff14d', 'emailAddress': '', 'totalAttendanceInSeconds': 2600, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '61a109a3-7049-4a35-9e24-e816f08ff14d', 'displayName': '柏天 (114514)   (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:07:28.9778518Z', 'leaveDateTime': '2022-12-16T01:50:49.3343481Z', 'durationInSeconds': 2600}]}, {'id': '2f246b6f-d35a-40bb-8164-add1d9c3ecff', 'emailAddress': '', 'totalAttendanceInSeconds': 1131, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '2f246b6f-d35a-40bb-8164-add1d9c3ecff', 'displayName': '石', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:07:30.2106849Z', 'leaveDateTime': '2022-12-16T01:26:22.0571304Z', 'durationInSeconds': 1131}]}, {'id': 'c228d473-67c1-4f4d-9e44-34bfecf0c29c', 'emailAddress': '', 'totalAttendanceInSeconds': 2591, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'c228d473-67c1-4f4d-9e44-34bfecf0c29c', 'displayName': '叶陈果 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:07:34.2917995Z', 'leaveDateTime': '2022-12-16T01:50:45.5335895Z', 'durationInSeconds': 2591}]}, {'id': '3b846109-e73e-4719-acb1-e6eeb7ec4a7e', 'emailAddress': '', 'totalAttendanceInSeconds': 2836, 'role': 'Attendee', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '3b846109-e73e-4719-acb1-e6eeb7ec4a7e', 'displayName': '31柯圣劼 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:07:38.2272281Z', 'leaveDateTime': '2022-12-16T01:54:55.1766711Z', 'durationInSeconds': 2836}]}, {'id': '22cea7bb-6462-4983-b173-0dc1fad7363e', 'emailAddress': '', 'totalAttendanceInSeconds': 2594, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '22cea7bb-6462-4983-b173-0dc1fad7363e', 'displayName': '费丞譞   (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:07:55.3883739Z', 'leaveDateTime': '2022-12-16T01:51:10.2365319Z', 'durationInSeconds': 2594}]}, {'id': '22819aa2-2815-473d-9309-d8dbee13242e', 'emailAddress': '', 'totalAttendanceInSeconds': 2542, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '22819aa2-2815-473d-9309-d8dbee13242e', 'displayName': '胡雯宁 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:08:29.9861524Z', 'leaveDateTime': '2022-12-16T01:50:52.492989Z', 'durationInSeconds': 2542}]}, {'id': '6699f8d9-e061-42b5-ad74-e82ad1447806', 'emailAddress': '', 'totalAttendanceInSeconds': 2542, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '6699f8d9-e061-42b5-ad74-e82ad1447806', 'displayName': '李禹璇 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:08:51.7606906Z', 'leaveDateTime': '2022-12-16T01:51:14.0953067Z', 'durationInSeconds': 2542}]}, {'id': '89b03873-1d28-4edd-aead-4ef7f6845613', 'emailAddress': '', 'totalAttendanceInSeconds': 2485, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '89b03873-1d28-4edd-aead-4ef7f6845613', 'displayName': '李鸿基 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:09:27.0803529Z', 'leaveDateTime': '2022-12-16T01:50:52.8442963Z', 'durationInSeconds': 2485}]}, {'id': '1e7d429d-a7c6-4c8b-a3a6-d5b43e1d1ca6', 'emailAddress': '', 'totalAttendanceInSeconds': 2486, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '1e7d429d-a7c6-4c8b-a3a6-d5b43e1d1ca6', 'displayName': '王者49 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:09:46.7282995Z', 'leaveDateTime': '2022-12-16T01:51:13.0635429Z', 'durationInSeconds': 2486}]}, {'id': '318013c9-84fa-46de-9b93-be7c9f9f5eba', 'emailAddress': '', 'totalAttendanceInSeconds': 2442, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '318013c9-84fa-46de-9b93-be7c9f9f5eba', 'displayName': '郭婧萱', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:10:01.2587379Z', 'leaveDateTime': '2022-12-16T01:50:44.1200548Z', 'durationInSeconds': 2442}]}, {'id': '07cc3d63-5357-4613-8eb7-7d204efbbd44', 'emailAddress': '', 'totalAttendanceInSeconds': 81, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '07cc3d63-5357-4613-8eb7-7d204efbbd44', 'displayName': '李凯文', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:11:31.8543967Z', 'leaveDateTime': '2022-12-16T01:12:53.1892563Z', 'durationInSeconds': 81}]}, {'id': '8b800c47-0edc-48ab-97c9-4d1be0f50ac6', 'emailAddress': '', 'totalAttendanceInSeconds': 1451, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '8b800c47-0edc-48ab-97c9-4d1be0f50ac6', 'displayName': '李凯文', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:12:19.6051985Z', 'leaveDateTime': '2022-12-16T01:36:31.367908Z', 'durationInSeconds': 1451}]}, {'id': '0508b52f-c6fc-497b-a520-4ea5f30752bc', 'emailAddress': '', 'totalAttendanceInSeconds': 704, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '0508b52f-c6fc-497b-a520-4ea5f30752bc', 'displayName': '石', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:25:49.1194333Z', 'leaveDateTime': '2022-12-16T01:37:33.1476334Z', 'durationInSeconds': 704}]}, {'id': 'd793be06-1fb9-4201-9c2b-3ec1ec9013cb', 'emailAddress': '', 'totalAttendanceInSeconds': 1470, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'd793be06-1fb9-4201-9c2b-3ec1ec9013cb', 'displayName': '高家宜 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:26:16.5131974Z', 'leaveDateTime': '2022-12-16T01:50:47.349584Z', 'durationInSeconds': 1470}]}, {'id': '5d355384-eb04-49d5-bdbc-8fff2b90208b', 'emailAddress': '', 'totalAttendanceInSeconds': 1026, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '5d355384-eb04-49d5-bdbc-8fff2b90208b', 'displayName': '俞玟溪 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:33:51.2212394Z', 'leaveDateTime': '2022-12-16T01:50:58.1164589Z', 'durationInSeconds': 1026}]}, {'id': '2d425cea-f54c-4049-9519-6128d34193e1', 'emailAddress': '', 'totalAttendanceInSeconds': 854, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '2d425cea-f54c-4049-9519-6128d34193e1', 'displayName': '李凯文', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:36:35.5779824Z', 'leaveDateTime': '2022-12-16T01:50:50.1932089Z', 'durationInSeconds': 854}]}, {'id': '3a1450f5-d4c2-416a-9ffb-34d97533c9c3', 'emailAddress': '', 'totalAttendanceInSeconds': 776, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '3a1450f5-d4c2-416a-9ffb-34d97533c9c3', 'displayName': '石', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:37:46.4062165Z', 'leaveDateTime': '2022-12-16T01:50:42.5632265Z', 'durationInSeconds': 776}]}, {'id': 'be2d08d0-b757-495c-bb59-02f459a12b37', 'emailAddress': '', 'totalAttendanceInSeconds': 532, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': 'be2d08d0-b757-495c-bb59-02f459a12b37', 'displayName': '陆佳琳 (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:42:05.3878783Z', 'leaveDateTime': '2022-12-16T01:50:57.6013928Z', 'durationInSeconds': 532}]}, {'id': '45373475-e5d8-4a31-b88c-4957947e2c4e', 'emailAddress': '', 'totalAttendanceInSeconds': 18, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '45373475-e5d8-4a31-b88c-4957947e2c4e', 'displayName': '王浩37', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:51:18.8415346Z', 'leaveDateTime': '2022-12-16T01:51:37.054663Z', 'durationInSeconds': 18}]}, {'id': '7f8e451b-8a9c-4486-a02d-957b3d916f34', 'emailAddress': '', 'totalAttendanceInSeconds': 4, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '7f8e451b-8a9c-4486-a02d-957b3d916f34', 'displayName': '方子欣  （VIP) (来宾)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:51:39.4210588Z', 'leaveDateTime': '2022-12-16T01:51:43.9235908Z', 'durationInSeconds': 4}]}, {'id': '923c5702-ffe0-45e9-bbf9-715caab4431e', 'emailAddress': '', 'totalAttendanceInSeconds': 72, 'role': 'Presenter', 'registrantId': None, 'identity': {'@odata.type': '#microsoft.graph.communicationsUserIdentity', 'id': '923c5702-ffe0-45e9-bbf9-715caab4431e', 'displayName': '111 (Guest)', 'tenantId': None}, 'attendanceIntervals': [{'joinDateTime': '2022-12-16T01:53:46.8754909Z', 'leaveDateTime': '2022-12-16T01:54:58.9688692Z', 'durationInSeconds': 72}]}]}
    result = get_attendance_by_json(json)
    print(result)