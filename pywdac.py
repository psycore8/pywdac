import argparse
import os
from shutil import copy
from subprocess import call
import utils.helper

prog_version = '0.1.5'
prog_header = f"""
             __    __  ___  _      ___ 
 _ __  _   _/ / /\\ \\ \\/   \\/_\\    / __\\
| '_ \\| | | \\ \\/  \\/ / /\\ //_\\\\  / \\/   
| |_) | |_| |\\  /\\  / /_//  _  \\/ /___ 
| .__/ \\__, | \\/  \\/___,'\\_/ \\_/\\____/ 
|_|    |___/ Version: {prog_version} by psycore8                    
"""
prog_directory = ''
prog_reboot = False
prog_reboot_seconds = 60
wdac_pol = 'SiPolicy.p7b'

def main():
  tform = utils.helper.nstate
  print(f'{tform.HEADER}{prog_header}{tform.ENDC}')
  print(f'{tform.LINK}https://www.github.com/psycore8/pywdac{tform.ENDC}\n\n')

  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--directory', help=f'Path to CodeIntegrity folder, where {wdac_pol} should be deployed')
  parser.add_argument('-r', '--reboot', action='store_true', help=f'Optional reboot after deployment, delayed for {prog_reboot_seconds} seconds')
  parser.add_argument('-u', '--undo', action='store_true', help=f'Deletes {wdac_pol} from CodeIntegrity folder')
  args = parser.parse_args()

  prog_reboot = args.reboot
  if not args.directory:
    print(tform.TextFail('Please specify the CodeIntegrity folder'))
    exit()
  else:
    prog_directory = args.directory
    print(tform.TextOKGreen('Directory argument given'))
    print(tform.TextOKBlue('Checking write permissions...'))
    if not os.access(prog_directory, os.W_OK):
      print(tform.TextFail('Write access is denied for this folder!'))
      exit()
    else:
      print(tform.TextOKGreen('Write permissions granted!'))
    if not args.undo:
      print(tform.TextOKBlue(f'Trying to deploy {wdac_pol} to {prog_directory}...'))
      copy(wdac_pol, f'{prog_directory}\\{wdac_pol}')
      if os.path.exists(f'{prog_directory}\\{wdac_pol}'):
        print(tform.TextOKGreen(f'File deployed to {prog_directory}'))
      else:
        print(tform.TextFail('Error during deployment'))
        exit()
    else:
      print(tform.TextOKBlue(f'Trying to remove {wdac_pol} from {prog_directory}...'))
      os.remove(f'{prog_directory}\\{wdac_pol}')
      if not os.path.exists(f'{prog_directory}\\{wdac_pol}'):
        print(tform.TextOKGreen(f'File deleted from {prog_directory}'))
      else:
        print(tform.TextFail('Error during delete operation'))
        exit()

    if prog_reboot:
      print(tform.TextInfo('Reboot flag is set...'))
      call(f'shutdown /r /t {prog_reboot_seconds}')
      print(tform.TextInfo(f'Reboot should begin in {prog_reboot_seconds} seconds, abort with shutdown -a'))

    print(tform.TextOKGreen('DONE!'))



if __name__ == "__main__":
  main()