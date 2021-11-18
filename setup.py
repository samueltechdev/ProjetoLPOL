import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()
   
setuptools.setup(
   name='ProjetoLPOL',
   version='0.0.1',
   author="Samuel Vancouver Foundation",
   author_email="VancouverCorp@VancouverCorp.com",
   description="Vamos testar essa bagaça",
   url="Your github URL",
   packages=["ProjetoLPOL"] or setuptools.find_packages(),
   classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
   ],
)