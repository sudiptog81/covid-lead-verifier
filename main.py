import re
import os
import cv2
import discord
import pytesseract
import numpy as np

from dotenv import load_dotenv

load_dotenv()


def preprocess(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold_img = cv2.threshold(
        gray_image, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU
    )[1]
    text = pytesseract.image_to_string(threshold_img)
    return text


class Client(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user.name, self.user.id)

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        else:
            if len(message.attachments) > 0:
                for attachment in message.attachments:
                    try:
                        image = cv2.imdecode(
                            np.asarray(
                                bytearray(await attachment.read()),
                                dtype='uint8'
                            ),
                            flags=cv2.COLOR_BGR2RGB
                        )
                        data = preprocess(image)
                        await message.reply(data)
                    except Exception as e:
                        await message.reply('Could not process text')


if __name__ == '__main__':
    client = Client()
    client.run(os.environ['DISCORD_TOKEN'])
