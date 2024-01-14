#
# print("Laboratorium 2")
# from deserialize_json import DeserializeJson
# newDeserializator = DeserializeJson('Assets/data.json')
# newDeserializator.somestats()
#
# from serialize_json import SerializeJson
# SerializeJson.run(newDeserializator, 'Assets/data_mod.json')
#
#
# from convert_json_to_yaml import ConvertJsonToYaml
# ConvertJsonToYaml.run(newDeserializator, 'Assets/data_mod.yaml')
import yaml

tempconffile = open('Assets/basic_config.yaml', encoding="utf8")
confdata = yaml.load(tempconffile, Loader=yaml.FullLoader)
print("Laboratorium 2")
from deserialize_json import DeserializeJson
from serialize_json import SerializeJson
from convert_json_to_yaml import ConvertJsonToYaml

if confdata['options']['source_type'] == 'file':
    newDeserializator = DeserializeJson(confdata['paths']['source_folder'] + confdata['paths']['json_source_file'])
else:
    data = {...}
    newDeserializator = DeserializeJson(data)

operations = confdata['options']['operations']

operations = sorted(operations, key=lambda oper: oper['position'])

for oper in operations:
    if oper['name'] == 'deserialize':
        deserialized_data = newDeserializator.data
        newDeserializator.somestats()
    elif oper['name'] == 'serialize':
        serializer = SerializeJson()
        SerializeJson.run(newDeserializator, 'Assets/data_mod2.json')
    elif oper['name'] == 'convert_to_yaml':
        converter = ConvertJsonToYaml()
        converter.run(deserialized_data, confdata['paths']['source_folder'] + confdata['paths']['yaml_destination_file'])
