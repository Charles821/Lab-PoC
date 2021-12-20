from flask_mail import Message
from . import mail


email_distribution = [
    'callatelaboca821@gmail.com',
]

normal_email_distribution = [
    'swiveldesk@hertz.com',
    'Lisa.Francis@lumen.com',

]
cc_email_distribution = [
    'Maurice.Campbell@lumen.com',
    'MESHertz-Engineering@centurylink.com',

]

def send_mail(message):
    """
    This function is intended to generate a text email of all change request details.
    """
    global email_distribution, cc_email_distribution, normal_email_distribution
    if message['swivel_desk'] == 'yes':
        normal_email_distribution.remove('swiveldesk@hertz.com')
    msg = Message("Change Request for Hertz " + message['title'], sender= "changecontrol@hertz.com",
                    recipients= email_distribution)
    msg.html = "<H1>Change Request for Hertz</H1><br>\
                    <b>Change type: </b> " + message['change_type'] + "<br>\
                    <b>Owner Name: </b> " + message['owner_name'] + "<br>\
                    <b>Vendor Name: </b> " + message['vendor'] + "<br>\
                    <b> Change Title: </b> " + message['title'] + "<br>\
                    <b>Technical Contact: </b> " + message['technical_contact_email'] + "<br>\
                    <b>Start (YYYY-MM-DD) Central Time: </b> " + str(message['start_date']) + "<br>\
                    <b>End (YYY-MM-DD) Central Time: </b> " + str(message['end_date']) + "<br>\
                    <b>Summary of Change: </b> " + message['summary'] + "<br>\
                    <b>Urgency of Change: </b> " + message['urgency'] + "<br>\
                    <b>Failure Probability: </b> " + message['failure_probability'] + "<br>\
                    <b>Impact of Change: </b> " + message['impact'] + "<br>\
                    <b>Details of Network Impact: </b> " + message['network_impact_details'] + "<br>\
                    <b>Change Justification: </b> " + message['justification'] + "<br>\
                    <b>Implementation Steps: </b> " + message['implementation_plan'] + "<br>\
                    <b>Test Plan: </b> " + message['test_plan'] + "<br>\
                    <b>Rollback Plan: </b> " + message['rollback_plan'] + "<br>"
    mail.send(msg)
    return "Message Sent!"

def status_mail(message):
    """
    This function generates a table of change request details.
    """
    global email_distribution, cc_email_distribution, normal_email_distribution, add_distribution
    msg = Message("Change Request for Hertz " + message['title'], sender="changecontrol@hertz.com",
                  recipients=email_distribution
                  )
    msg.html = "<html>\
                    <head>\
                        <style>\
                            td {border: 1px solid black;}\
                        </style>\
                    <body style=\"background-color: #ffffff; min-height=400px;\">\
                    <H1>Change Request Info</H1><br>\
                    <table role=\"presentation\"style=\"border:1px solid black; border-collapse:collapse; width: 80%;\">\
                    <tr style=\"background-color:#FFFFE0;\">\
                            <td colspan=\"3\"><b>Title</b></td>\
                        </tr>\
                    <tr>\
                        <td colspan=\"3\">" + message['title'] + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                            <td><b>Change type</b></td>\
                            <td colspan=\"2\"><b>Exclude Swivel Desk?</b></td>\
                        </tr>\
                    <tr>\
                        <td>" + message['change_type'] + "</td>\
                        <td colspan=\"2\">" + message['swivel_desk'] + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td><b>Owner of Change</b></td>\
                        <td><b>Vendor</b></td>\
                        <td><b>Technical Contact Email</b></td>\
                    </tr>\
                    <tr>\
                        <td>" + message['owner_name'] + "</td>\
                        <td>" + message['vendor'] + "</td>\
                        <td>" + message['technical_contact_email'] + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td colspan=\"3\"><b>Start (YYYY-MM-DD) Central Time</b></td>\
                    </tr>\
                    <tr>\
                        <td colspan=\"3\">" + str(message['start_date']) + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td colspan=\"3\"><b>Stop (YYYY-MM-DD) Central Time</b></td>\
                    </tr>\
                    <tr>\
                        <td colspan=\"3\">" + str(message['end_date']) + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td colspan=\"3\"><b>Summary of Change</b></td>\
                    </tr>\
                    <tr>\
                        <td colspan=\"3\">" + message['summary'] + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td><b>Urgency of Change</b></td>\
                        <td><b>Failure Probability</b></td>\
                        <td><b>Impact of Change</b></td>\
                    </tr>\
                    <tr>\
                        <td>" + message['urgency'] + "</td>\
                        <td>" + message['failure_probability'] + "</td>\
                        <td>" + message['impact'] + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td colspan=\"3\"><b>Details of Network Impact</b></td>\
                    </tr>\
                    <tr>\
                        <td colspan=\"3\">" + message['network_impact_details'] + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td colspan=\"3\"><b>Change Justification</b></td>\
                    </tr>\
                    <tr>\
                        <td colspan=\"3\">" + message['justification'] + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td colspan=\"3\"><b>Implementation Steps</b></td>\
                    </tr>\
                    <tr>\
                        <td colspan=\"3\">" + message['implementation_plan'] + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td colspan=\"3\"><b>Test Plan</b></td>\
                    </tr>\
                    <tr>\
                        <td colspan=\"3\">" + message['test_plan'] + "</td>\
                    </tr>\
                    <tr style=\"background-color:#FFFFE0;\">\
                        <td colspan=\"3\"><b>Rollback Plan</b></td>\
                    </tr>\
                    <tr>\
                        <td colspan=\"3\">" + message['rollback_plan'] + "</td>\
                    </tr>\
                    </table>\
                    </body>\
                    </html>"
    mail.send(msg)
    return "Message Sent!"


def summary_mail(message, summary_list):
    """
    This function is intended to generate a summary table for weekly delivery.
    """
    global email_distribution, cc_email_distribution, normal_email_distribution, add_distribution
    detail_string2 = ''
    detail_string = ''

    for index in summary_list:
        for val1 in index.values():
            detail_string += """<tr>""" + '\n'
            detail_string += """<td>""" + val1['start_date'] + """</td>""" + '\n'
            detail_string += """<td>""" + val1['title'] + """</td>""" + '\n'
            detail_string += """<td>""" + val1['network_impact_details'] + """</td>""" + '\n'
            detail_string += """</tr>""" + '\n'

    detail_string2 += """<html>""" + '\n'
    detail_string2 += """<head>""" + '\n'
    detail_string2 += """<style>""" + '\n'
    detail_string2 += """td {border: 1px solid black;}""" + '\n'
    detail_string2 += """</style>""" + '\n'
    detail_string2 += """<body style=background-color: #80aaff; min-height=400px;>""" + '\n'
    detail_string2 += """<H1>Change Request Info</H1><br>""" + '\n'
    detail_string2 += """<table role=presentation style=border:1px solid black; border-collapse:collapse; width: 80%;>""" + '\n'
    detail_string2 += """<tr style=background-color:#FFFFE0;>""" + '\n'
    detail_string2 += """<td><b>Date of Change</b></td>""" + '\n'
    detail_string2 += """<td><b>Title</b></td>""" + '\n'
    detail_string2 += """<td><b>Network Impact</b></td>""" + '\n'
    detail_string2 += """<td><b>Service Request</b></td>""" + '\n'
    detail_string2 += """<td><b>Hertz Change</b></td>""" + '\n'
    detail_string2 += """</tr>""" + '\n'
    if message['swivel_desk'] == 'yes':
        normal_email_distribution.remove('swiveldesk@hertz.com')
    msg = Message("Change Control Activities", sender="changecontrol@hertz.com",
                  recipients=email_distribution
                  )
    print(changes)

    msg.html = detail_string2
    msg.html += detail_string
    msg.html += "</table>\
                    </body>\
                    </html>"
    mail.send(msg)
    return "Message Sent!"