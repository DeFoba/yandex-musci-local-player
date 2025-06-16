from DrissionPage import ChromiumOptions, ChromiumPage
import re, time, requests



class Browser:
    def __init__(self):
        print('LOG: Starting/Connect Browser')
        self.PROFILE_PATH = 'music_browser'

        self.co = ChromiumOptions()
        self.co.arguments.append('--my-program')
        self.co.set_user_data_path(self.PROFILE_PATH)

        self.page = ChromiumPage(addr_or_opts=self.co)
        print('LOG: Opening "music.yandex.ru"...')
        self.open_music()

        print('LOG: Finding controlls...')
        time.sleep(10)
        self.controlls = self.find_controlls()

        print('LOG: Get Track Info...')
        self.get_track_info()
        

    def open_music(self):
        self.page.get('https://music.yandex.ru/')

    def download_img(self, url):
        with open('static/track_img.jpg', 'wb') as track_img:
            track_img.write(requests.get(url).content)

    def play(self):
        self.play_track_btn.click()
        self.find_controlls()

    def next(self):
        self.next_track_btn.click()
        self.find_controlls()

    def back(self):
        self.back_track_btn.click()
        self.find_controlls()

    def find_controlls(self):
        self.player = self.page.ele('tag:div@@class^BaseSonataControlsDesktop_sonataButtons')
        self.back_track_btn, self.play_track_btn, self.next_track_btn = self.player.eles('tag:button')
        # print('-'*5, 'RESULT', '-'*5)
        # print(self.player, self.next_track_btn.attr('aria-label'), self.back_track_btn.attr('aria-label'), self.play_track_btn.attr('aria-label'), sep='\n')
        # self.next_track_btn.click()
        return self.back_track_btn, self.play_track_btn, self.next_track_btn

    def get_track_info(self):
        self.card = self.page.ele('tag:div@@class^PlayerBarDesktop_infoCard')
        self.track_image_link = self.card.ele('tag:img').attr('src').replace('100x100', '400x400')
        # self.download_img(self.track_image_link)
        self.track_name = self.card.ele('tag:div@@class^Meta_titleContainer').text
        self.group_name = self.card.ele('tag:div@@class^SeparatedArtists_root_variant_breakAll').text

        # print(self.track_name, self.group_name)
        return self.track_name, self.group_name, self.track_image_link


if __name__ == '__main__':
    Browser()