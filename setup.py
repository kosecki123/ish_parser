from distutils.core import setup

setup(name='ish_parser',
      version='0.0.6',
      author_email='thayden@gmail.com, piotrkosinski@gmail.com',
      description='Parser for NOAA ISH (integrated surface hourly) reports',
      author='thayden, kosecki123',
      url='https://github.com/kosecki123/ish_parser',
      package_dir={'ish_parser': 'src'},
      py_modules=['ish_parser', 'ish_report', 'Temperature', 'Observation', 'Units', 'Components', 'Distance', 'Speed', 'Direction', 'Pressure', 'ReportType', 'Humidity'])
