## *********************************************************
## 
## File autogenerated for the aravis_camera_driver package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

##**********************************************************
## Software License Agreement (BSD License)
##
##  Copyright (c) 2008, Willow Garage, Inc.
##  All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions
##  are met:
##
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above
##     copyright notice, this list of conditions and the following
##     disclaimer in the documentation and/or other materials provided
##     with the distribution.
##   * Neither the name of the Willow Garage nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
##  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
##  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
##  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
##  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
##  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
##  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
##  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##**********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 259, 'description': 'Capture mode', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'capture_mode', 'edit_method': "{'enum_description': 'Enum to set the capture mode.', 'enum': [{'srcline': 12, 'description': 'Continuous', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'continuous', 'ctype': 'std::string', 'type': 'str', 'name': 'Continuous'}, {'srcline': 13, 'description': 'Triggered', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'triggered', 'ctype': 'std::string', 'type': 'str', 'name': 'Triggered'}]}", 'default': 'continuous', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'Trigger source', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'trigger_source', 'edit_method': "{'enum_description': 'Enum to set the trigger source.', 'enum': [{'srcline': 16, 'description': 'Line 1', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'Line1', 'ctype': 'std::string', 'type': 'str', 'name': 'Line1'}, {'srcline': 17, 'description': 'Line 2', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'Line2', 'ctype': 'std::string', 'type': 'str', 'name': 'Line2'}]}", 'default': 'Line1', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'Trigger activation', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'trigger_activation', 'edit_method': "{'enum_description': 'Enum to set the trigger activation.', 'enum': [{'srcline': 20, 'description': 'Rising edge', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'RisingEdge', 'ctype': 'std::string', 'type': 'str', 'name': 'RisingEdge'}, {'srcline': 21, 'description': 'Falling edge', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'FallingEdge', 'ctype': 'std::string', 'type': 'str', 'name': 'FallingEdge'}]}", 'default': 'RisingEdge', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'Frame rate', 'max': 400, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'frame_rate', 'edit_method': '', 'default': 30, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 259, 'description': 'Exposure mode', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'exposure_auto', 'edit_method': "{'enum_description': 'Enum to set the exposure mode.', 'enum': [{'srcline': 25, 'description': 'Auto exposure', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'auto', 'ctype': 'std::string', 'type': 'str', 'name': 'AutoExposure'}, {'srcline': 26, 'description': 'Auto once exposure', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'auto_once', 'ctype': 'std::string', 'type': 'str', 'name': 'AutoOnceExposure'}, {'srcline': 27, 'description': 'Fixed exposure', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'fixed', 'ctype': 'std::string', 'type': 'str', 'name': 'FixedExposure'}]}", 'default': 'auto', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'Exposure (us)', 'max': 65520, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'exposure_time', 'edit_method': '', 'default': 1000, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 259, 'description': 'Gain mode', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'gain_mode', 'edit_method': "{'enum_description': 'Enum to set the gain mode.', 'enum': [{'srcline': 30, 'description': 'Auto gain', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'auto', 'ctype': 'std::string', 'type': 'str', 'name': 'AutoGain'}, {'srcline': 31, 'description': 'Auto once gain', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'auto_once', 'ctype': 'std::string', 'type': 'str', 'name': 'AutoOnceGain'}, {'srcline': 32, 'description': 'Fixed gain', 'srcfile': '../cfg/BaslerCamera.cfg', 'cconsttype': 'const char * const', 'value': 'fixed', 'ctype': 'std::string', 'type': 'str', 'name': 'FixedGain'}]}", 'default': 'auto', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'Gain', 'max': 500, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'gain', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'Auto white balance once', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'auto_white_balance_once', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'Digital shift', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'digital_shift', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

BaslerCamera_Continuous = 'continuous'
BaslerCamera_Triggered = 'triggered'
BaslerCamera_Line1 = 'Line1'
BaslerCamera_Line2 = 'Line2'
BaslerCamera_RisingEdge = 'RisingEdge'
BaslerCamera_FallingEdge = 'FallingEdge'
BaslerCamera_AutoExposure = 'auto'
BaslerCamera_AutoOnceExposure = 'auto_once'
BaslerCamera_FixedExposure = 'fixed'
BaslerCamera_AutoGain = 'auto'
BaslerCamera_AutoOnceGain = 'auto_once'
BaslerCamera_FixedGain = 'fixed'
