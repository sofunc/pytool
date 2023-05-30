import os
import xml.etree.ElementTree as ET

for filename in os.listdir('apks'):
    if filename.endswith('.xml'):
        try:
            tree = ET.parse(os.path.join('apks', filename))
            root = tree.getroot()
            # 检查debuggable标记
            if 'android:debuggable' in root.attrib and root.attrib['android:debuggable'] == 'true':
                print(f'{filename} 存在 debuggable=true 安全风险!')
            # 检查allowBackup标记
            if 'android:allowBackup' in root.attrib and root.attrib['android:allowBackup'] == 'true':
                print(f'{filename} 存在 allowBackup=true 安全风险!')
            # 其他检查...
        except ET.ParseError as err:
            print(f'解析 {filename} 发生错误:{err}')