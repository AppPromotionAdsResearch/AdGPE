import time
# import uiautomator2 as u2
from .input_event import TouchEvent
import os


def simplify_event_str(event_str):
    'TouchEvent(state=43bda44fb88f8ec3d98bf0f17f2d4263, view=460016931d4363b29e86167b2c3f9ec1(MainActivity/TextView-Open))'
    if 'BACK' in event_str:
        return event_str
    elif 'TouchEvent' in event_str:
        sections=event_str.split('(')
        return sections[0]+'(('+sections[2]
    else:
        return event_str
def contain_ad_text(possible_events,ad_buttons):
    for event in possible_events:
        view = event.view
        view_text = view['text'] if view['text'] is not None else ''
        view_text = view_text.lower().strip()
        # Events with view_text in self.ad_buttons get priority
        if view_text in ad_buttons:
            return True
    return False

def sort_ad_events(possible_events,ad_buttons):

    def sort_key(event):
        view = event.view
        view_text = view['text'] if view['text'] is not None else ''
        view_text = view_text.lower().strip()
        # Events with view_text in self.ad_buttons get priority
        return view_text not in ad_buttons

    # Sort the possible_events in place
    possible_events.sort(key=sort_key)
    return possible_events


def findPackage_droidbot(current_state,self):
    for view in current_state.views:
        content_descrip=view.get('text')
        if content_descrip!=None:
            if content_descrip.lower()=='more info':
                TouchEvent(view=view).send(self.device)
                self.logger.info("Go to google play")
                time.sleep(1)
                break
            # elif 'pub' in content_descrip.lower():

    views = self.device.get_views()
    for view in views:
        content_descrip=view.get('content_description')
        if content_descrip!=None:
            if content_descrip.lower()=='more options':
                TouchEvent(view=view).send(self.device)
                self.logger.info("Clicking three dots")
                time.sleep(1)
                break

    # current_state=self.device.get_current_state()
    views=self.device.get_views()
    for view in views:
        content_descrip=view.get('text')
        if content_descrip!=None:
            if content_descrip.lower()=='share':
                TouchEvent(view=view).send(self.device)
                self.logger.info("Clicking Share")
                time.sleep(2)
                break
    views=self.device.get_views()
    serial_number = current_state.device.serial
    for view in views:
        content_descrip=view.get('text')
        if content_descrip!=None:
            if content_descrip.lower()=='copy url':
                TouchEvent(view=view).send(self.device)
                self.logger.info("Clicking Copy URL")
                # d.app_start('ca.zgrs.clipper')
                os.popen('adb -s {} shell am start -n ca.zgrs.clipper/.Main'.format(serial_number))
                time.sleep(1)
                cmdOutput = os.popen('adb -s {} shell am broadcast -a clipper.get'.format(serial_number))
                intent=cmdOutput.read()
                packageName=intent.split('id=')[-1][:-2]

                self.ads.append(packageName)
                self.logger.info("Advertising: {}".format(packageName))
                break
# def findPackage_u2(current_state,self):
#     packageName = False
#     serial_number=current_state.device.serial
#     d=u2.connect(serial_number)
#     # time.sleep(1)
#     if d(text="More info").count > 0:
#         d(text='More info').click()
#         time.sleep(1)
#     # for Android 9, it doesn't always show more info
#     # else:
#     #     return 0
#
#     d.xpath("//android.widget.TextView").wait(1)
#
#     if d.xpath('//*[@content-desc="More options"]').exists:
#         d.xpath('//*[@content-desc="More options"]').click()
#         time.sleep(1)
#
#     if d.xpath('//*[@content-desc="More Options"]').exists:
#         d.xpath('//*[@content-desc="More Options"]').click()
#         time.sleep(1)
#
#     if d(text='Share').count>0:
#         # click Share
#         d(text='Share')[0].click()
#         # click copy to clipboard
#         time.sleep(1)
#
#         d(text='Copy URL')[0].click()
#         d.app_start('ca.zgrs.clipper')
#         time.sleep(1)
#         cmdOutput = os.popen('adb -s {} shell am broadcast -a clipper.get'.format(serial_number))
#         intent=cmdOutput.read()
#         packageName=intent.split('id=')[-1][:-2]
#
#
#
#     self.ads.append(packageName)
