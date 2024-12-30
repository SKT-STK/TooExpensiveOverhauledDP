import json
import os

DIR = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\.fabric\remappedJars\minecraft-1.21.3-0.16.9\client-intermediary\data\minecraft\recipe'
OUT = r'D:\Games\Minecraft\ModrinthApp\profiles\NIGGER\saves\remove_too_expensive_dp\datapacks\RemoveTooExpensiveDP\data\teodp\recipe'

MATERIALS = [
  'iron',
  'diamond',
  'netherite'
]

things = []
for filename in os.listdir(DIR):
  if filename.endswith('_smithing.json'):
    with open(os.path.join(DIR, filename)) as file:
      things.append(json.load(file)['result']['id'].split('_')[1])
    
niggers = []
for thing in things:
  for material in MATERIALS:
    recipe = dict(
      type = 'minecraft:smithing_transform',
      base = f'minecraft:{material}_{thing}',
      addition = 'minecraft:echo_shard',
      template = 'minecraft:jigsaw',
      result = dict(
        id = f'minecraft:{material}_{thing}',
        components = dict()
      )
    )
    recipe['result']['components']['!minecraft:repair_cost'] = {}

    niggers.append(dict(filename = f'{material}_{thing}', recipe = recipe))
    
for nigger in niggers:
  with open(os.path.join(OUT, nigger['filename'] + '.json'), 'w') as file:
    json.dump(nigger['recipe'], file, indent = 4)
