import random
import yaml
import string
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class TemplateModel:

    def __init__(self, app=None):
        self.app = app

    def generate_template(self, buttons=1):
        zip = []
        for i in range(buttons):
            zip.append(
                {"id": random.randint(1, 1000000), "label": self.get_str(), "link": "https://stackoverflow.com/"})
        with open(ROOT_DIR + f'/data/{self.get_str()}.yaml', 'w') as outfile:
            yaml.dump(zip, outfile, default_flow_style=False)
            # print(os.path.splitext(os.path.basename(outfile.name))[0])
            return os.path.splitext(os.path.basename(outfile.name))[0]

    def generate_wrong_template(self):
        zip = []
        zip.append(
            {"2label2": self.get_str(), "2link2": "https://stackoverflow.com/"})
        with open(ROOT_DIR + f'/data/{self.get_str()}.yaml', 'w') as outfile:
            yaml.dump(zip, outfile, default_flow_style=False)
            # print(os.path.splitext(os.path.basename(outfile.name))[0])
            return os.path.splitext(os.path.basename(outfile.name))[0]

    def generate_wrong_format(self):
        zip = []
        zip.append(
            {"id": random.randint(1, 1000000), "label": self.get_str(), "link": "https://stackoverflow.com/"})
        with open(ROOT_DIR + f'/data/{self.get_str()}.txt', 'w') as outfile:
            yaml.dump(zip, outfile, default_flow_style=False)
            return ''.join(os.path.splitext(os.path.basename(outfile.name)))
            # return os.path.splitext(os.path.basename(outfile.name))[0]

    def get_str(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


if __name__ == "__main__":
    s = TemplateModel()
    s.generate_wrong_format()
