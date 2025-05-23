# Building ComplianceAsCode

## Fast Track
Ok, if you are eager to start contributing, seeing the things happening faster and are passionate about automation, this is what you need for now. Every technical procedure described in the next sessions of this guide is covered by the [openscap](https://galaxy.ansible.com/ui/standalone/roles/marcusburghardt/openscap/) role.

Do you prefer to see it working before starting to use it? Please, take a look in this demo:
[![ansible-role-openscap demo](https://img.youtube.com/vi/YI5lo1P0gw0/3.jpg)](http://www.youtube.com/watch?v=YI5lo1P0gw0 "watch an ansible-role-openscap demo")

### ansible-role-openscap
Everything you need as requirement is a *Fedora* system with the `ansible` and `python3` packages installed:
```bash
dnf install -y ansible python3
```
Then you can download the ansible role:
```bash
ansible-galaxy install marcusburghardt.openscap
```
Now it is time to run it. To help with this, the function also comes with a pre-configured Ansible environment for this. It is recommended to use this environment in order to ensure that it is only applicable to this context, not impacting any other possible Ansible settings you may have on your computer:
```bash
cp -r ~/.ansible/roles/marcusburghardt.openscap/files/Ansible_Samples/ ~/Ansible
cd ~/Ansible/
ansible-playbook -K ansible_openscap.yml
```
Just watch the ansible do the hard work. In the end, you will have a "ready to go" development environment to start [contributing](https://github.com/ComplianceAsCode/content/blob/master/CONTRIBUTING.md). If this is your first contact with the project, there is also a "STARTGUIDE" to guide you through the newly prepared development environment:
```bash
less ~/OpenSCAP/STARTGUIDE.md
```


## Installing build dependencies

### Required Dependencies
On *Red Hat Enterprise Linux 8* and *Fedora* the package list but must also include python3:

```bash
dnf install cmake make openscap-utils openscap-scanner python3 python3-setuptools
```

On *Ubuntu* and *Debian*, make sure the packages `libopenscap8`,
`libxml2-utils`, `xsltproc` and their dependencies are installed:

```bash
apt-get install cmake make libopenscap8 libxml2-utils ninja-build xsltproc
```

IMPORTANT: Version `1.0.8` or later of `openscap-utils` is required to build the content.

### Python Dependencies

Some python dependencies must be installed through pip because they're not
packaged by a distribution.

Dependencies for developing are in `requirements.txt` and you can install them using:

```bash
$ pip3 install -r requirements.txt
```

Test dependencies are kept in a separate requirements file called
`test-requirements.txt` and are installed using the same process:

```bash
$ pip3 install -r test-requirements.txt
```

### Git (Clone the Repository)

Install git if you want to clone the GitHub repository to get the
source code:

```bash
# Fedora/RHEL
yum install git

# Ubuntu/Debian
apt-get install git
```

### Shellcheck (Script Static Analysis)

Install the `ShellCheck` package to perform fix script static analysis:

```bash
# Fedora/RHEL
yum install ShellCheck

# Ubuntu/Debian
apt-get install shellcheck
```

### Bats (Bash Unit Tests)

Install the `bats` package to perform bash unit tests:

```bash
# Fedora/RHEL
yum install bats

# Ubuntu/Debian
apt-get install bats
```

### xmldiff (Python unit tests)

Install the `lxml` package to execute Python unit tests that use these packages.

```bash
# Fedora/RHEL
yum install python3-lxml

# Ubuntu/Debian
apt-get install python-lxml
```

### Ansible Static Analysis packages

Install `yamllint` and `ansible-lint` packages to perform Ansible
playbooks checks. These checks are not enabled by default in CTest, to enable
them add `-DANSIBLE_CHECKS=ON` option to `cmake`.
```bash
# Fedora/RHEL
yum install yamllint ansible-lint

# Ubuntu/Debian (to install ansible-lint on Debian you will probably need to
# enable Debian Backports repository)
apt-get install yamllint ansible-lint
```

### Static Ansible Playbooks tests

Install `pytest` to run tests cases that analyse the Ansible
Playbooks' yaml nodes.
```bash
# Fedora/RHEL
yum install python3-pytest

# Ubuntu/Debian
apt-get install python-pytest
```

### Ninja (Faster Builds)

Install the `ninja` build system if you want to use it instead of
`make` for faster builds:

```bash
# Fedora/RHEL
yum install ninja-build

# Ubuntu/Debian
apt-get install ninja-build
```

### Sphinx packages (Developer Documentation)

Building docs can be done via tox file or manually.  Note that tox creates a
virtual environment to handle all dependencies defined in the docs requirements
file.

#### Using the tox file

```bash
# Fedora/RHEL
yum install tox

# Ubuntu/Debian
apt-get install tox
```

```bash
tox -e docs
```

#### Manual method

Install Sphinx packages if you want to generate HTML Documentation, from source directory run:

```bash
# Fedora/RHEL
yum install python3-sphinx

# Ubuntu/Debian
apt-get install python3-sphinx
```

```bash
pip install -r docs/requirements.txt
```

```bash
make -C docs html
```

### Pandas (SRG Export HTML)

Install `pandas` if you want to run `utils/create_srg_export.py`:

```bash
# Fedora/RHEL
yum install python3-pandas

# Ubuntu/Debian
apt-get install python3-pandas
```

### OpenpyXL (SRG Export XLSX)

```bash
# Fedora/RHEL
yum install python3-openpyxl

# Ubuntu/Debian
apt-get install python3-openpyxl
```

### pygithub (Ansible Playbooks to Ansible roles)

```bash
# Fedora/RHEL
yum install python3-pygithub

# Ubuntu/Debian
apt-get install python3-pygithub
```

### mypy (Static Typing)

```bash
# Fedora/RHEL
yum install python3-mypy

# Ubuntu/Debian
apt-get install python3-mypy
```

## Downloading the source code

Download and extract a tarball from the [list of releases](https://github.com/ComplianceAsCode/content/releases):

```bash
# change X.Y.Z for desired version
ssg_version="X.Y.Z"
wget "https://github.com/ComplianceAsCode/content/releases/download/v$ssg_version/scap-security-guide-$ssg_version.tar.bz2"
tar -xvjf ./scap-security-guide-$ssg_version.tar.bz2
cd ./scap-security-guide-$ssg_version/
```

Or clone the GitHub repository:

```bash
git clone https://github.com/ComplianceAsCode/content.git
cd content/
# (optional) select release version - change X.Y.Z for desired version
git checkout vX.Y.Z
# (optional) select latest development version
git checkout master
```

## Building

### Building Everything

To build all the security content:

```bash
cd build/
cmake ../
# To build all security content
make -j4
# To build security content for one specific product, for example for *Red Hat Enterprise Linux 9*
make -j4 rhel9
```

Or use the `build_product` script from the base directory that removes
whatever is in the `build` directory and builds a specific product:

```bash
./build_product rhel9
```

For more information about available options, call `./build_product --help`.

### Building Specific Content

To build specific content for a specific product:

```bash
cd build/
cmake ../
make -j4 rhel9-content  # SCAP XML files for RHEL9
make -j4 rhel9-guides  # HTML guides for RHEL9
make -j4 rhel9-tables  # HTML tables for RHEL9
make -j4 rhel9-profile-bash-scripts  # remediation Bash scripts for all RHEL9 profiles
make -j4 rhel9-profile-playbooks # Ansible Playbooks for all RHEL9 profiles
make -j4 rhel9  # everything above for RHEL9
```

### Building thin The Datastreams

A thin Datastream is a Datastream that contains only one rule with minimal SCAP parts, without any additional OVAL checks, XCCDF groups, profiles, and CPE checks.

This command will generate thin Datastreams for each rule for the product.
The thin Datastreams are located in the build `build/thin_ds` directory.

```bash
    ./build_product fedora --thin
```

This command generates a thin Datastream for the specific rule specified as a parameter.
The thin Datastream is stored under the normal Datastream name (for example, `ssg-fedora-ds.xml`).

```bash
    ./build_product fedora --rule-id enable_fips_mode
```

### Configuring CMake options using GUI

Configure options before building using a GUI tool:

```bash
cd build/
cmake-gui ../
make -j4
```

### Reproducible Builds

Set the environment variable `SOURCE_DATE_EPOCH` to generate [reproducible builds](https://reproducible-builds.org/).
For details about the values and meaning of this variable please check this [source](https://reproducible-builds.org/specs/source-date-epoch/):

```bash
cd build/
SOURCE_DATE_EPOCH=1614699939 make
```

### Using Ninja for Faster Builds

Use the `ninja` build system (requires the `ninja-build` package):

```bash
cd build/
cmake -G Ninja ../
ninja-build  # depending on the distribution just "ninja" may also work
```

### Generating Statistics for Products and Profiles

#### Text Output

Generate statistics for products and profiles. Some of the statistics generated are: implemented OVAL, bash, Ansible for rules, missing CCE, etc:

```bash
cd build/
cmake ../
make -j4 stats # display statistics in text format for all products
make -j4 profile-stats # display statistics in text format for all profiles in all products
```

You can also create statistics per product. Prepend the product name (e.g.: `rhel9-stats`) to the make target.

#### HTML Output

To generate an HTML output, run a similar command:

```bash
cd build/
cmake ../
make -j4 html-stats # generate statistics for all products, as a result <product>/product-statistics/statistics.html file is created.
make -j4 html-profile-stats # generate statistics for all profiles in all products, as a result <product>/profile-statistics/statistics.html file is created
```

If you want to go deeper into statistics, refer to [Profile Statistics and Utilities](manual/developer/05_tools_and_utilities.md#profile-statistics-and-utilities) section.


### Generating Sphinx Documentation
Generate HTML documentation of the project that includes developer documentation,
supported Jinja Macros documentation, python modules documentation, Automatus
documentation and release tools documentation:

```bash
cd build/
cmake ../
make -j4 docs # check docs/index.html file
```

### Building compliant SCAP 1.2 content

The build system builds SCAP content with OVAL 5.11.
This means that the SCAP 1.3 data stream conforms to SCAP standard version 1.3.
But the SCAP 1.2 data stream is not fully conformant with SCAP standard version 1.2, as up to OVAL 5.10 version is allowed.
As SCAP 1.3 allows up to OVAL 5.11 and SCAP 1.2 allows up to OVAL 5.10.
This project no longer builds content that is fully SCAP 1.2 compliant as we no longer support OVAL 5.10.
The last release supporting SCAP 1.2 content was [v0.1.64](https://github.com/ComplianceAsCode/content/releases/tag/v0.1.64).

### Building SCE (non-compliant) content

By default, the build system will try to build XCCDF/OVAL standards-compliant
content. To enable SCE content, specify the `-DSSG_SCE_ENABLED=ON` option to
CMake:

```bash
cd build
cmake -DSSG_SCE_ENABLED=ON ..
make
```

This will add SCE content into the data stream files as well as create the
`<product>/checks/sce` folder with individual SCE checks in it.

### Build outputs

When the build has completed, the output will be in the build folder.
That can be any folder you choose but if you followed the examples above
it will be the `content/build` folder.

### SCAP XML files

The SCAP XML files will be called `ssg-${PRODUCT}-${TYPE}.xml`. For example
`ssg-rhel9-ds.xml` is the SCAP 1.3 *Red Hat Enterprise Linux 9* **source data stream**.

We recommend using **source data stream** if you have a choice.
The build system also generates separate XCCDF, OVAL, OCIL and CPE files:

```bash
$ ls -1 ssg-rhel9-*.xml
ssg-rhel9-cpe-dictionary.xml
ssg-rhel9-cpe-oval.xml
ssg-rhel9-ds.xml
ssg-rhel9-ocil.xml
ssg-rhel9-oval.xml
ssg-rhel9-xccdf.xml
```

These can be ingested by any SCAP-compatible scanning tool, to enable automated
checking.

### HTML Guides

The human-readable HTML guide index files will be called
`ssg-${PRODUCT}-guide-index.html`. For example `ssg-rhel9-guide-index.html`.
This file will let the user browse all profiles available for that product.
The prose guide HTML contains practical, actionable information for auditors
and administrators. They are placed in the `guides` folder.
```bash
$ ls -1 guides/ssg-rhel9-*.html
guides/ssg-rhel9-guide-anssi_bp28_enhanced.html
guides/ssg-rhel9-guide-anssi_bp28_high.html
guides/ssg-rhel9-guide-anssi_bp28_intermediary.html
guides/ssg-rhel9-guide-anssi_bp28_minimal.html
guides/ssg-rhel9-guide-ccn_advanced.html
guides/ssg-rhel9-guide-ccn_basic.html
...
```

### HTML Reference Tables
Spreadsheet HTML tables - potentially useful as the basis for a
*Security Requirements Traceability Matrix (SRTM) document*:

```bash
$ ls -1 tables/table-rhel9-*.html
tables/table-rhel9-cces.html
tables/table-rhel9-srgmap-flat.html
tables/table-rhel9-srgmap.html
tables/table-rhel9-stig_gui-testinfo.html
tables/table-rhel9-stig.html
tables/table-rhel9-stig-manual.html
tables/table-rhel9-stig-testinfo.html
```

### Ansible Playbooks

#### Profile Ansible Playbooks
These Playbooks contain the remediations for a profile.
```bash
$ ls -1 ansible/rhel9-playbook-*.yml
ansible/rhel9-playbook-anssi_bp28_enhanced.yml
ansible/rhel9-playbook-anssi_bp28_high.yml
ansible/rhel9-playbook-anssi_bp28_intermediary.yml
ansible/rhel9-playbook-anssi_bp28_minimal.yml
ansible/rhel9-playbook-ccn_advanced.yml
ansible/rhel9-playbook-ccn_basic.yml
ansible/rhel9-playbook-ccn_intermediate.yml

...
```

#### Rule Ansible Playbooks
These Playbooks contain just the remediation for a rule, in the context of a profile.
```bash
$ ls -1 rhel9/playbooks/pci-dss/*.yml | head
rhel9/playbooks/pci-dss/account_disable_post_pw_expiration.yml
rhel9/playbooks/pci-dss/accounts_maximum_age_login_defs.yml
rhel9/playbooks/pci-dss/accounts_no_uid_except_zero.yml
rhel9/playbooks/pci-dss/accounts_password_pam_dcredit.yml
...
```
~~
#### Rule SCE Checks

These scripts contain SCE content for the specified rule.

```bash
$ ls -1 rhel9/checks/sce/
ip6tables_rules_for_open_ports.sh
iptables_rules_for_open_ports.sh
metadata.json
set_iptables_outbound_n_established.sh
set_nftables_base_chain.sh
set_nftables_table.sh
ssh_keys_passphrase_protected.sh
```

### Profile Bash Scripts
These Bash Scripts contains the remediations for a profile.
```bash
$ ls -1 bash/rhel9-script-*.sh
bash/rhel9-script-anssi_bp28_enhanced.sh
...
bash/rhel9-script-e8.sh
bash/rhel9-script-hipaa.sh
...
```

### Automatus Tests

You can build the Automatus tests so they can be run directly.
To enable build with `-DSSG_BUILT_TESTS_ENABLED:BOOL=ON`
The tests will be `$PRODUCT/tests/` with directory for each rule.

you can also use the `build_product` script together with `--render-test-scenarios` option.

## Testing

To ensure validity of built artifacts prior to installation, we recommend
running our test suite against the build output. This is done with CTest.
It is a good idea to execute quick tests first using the `-L quick` option passed to `ctest`.

```bash
cd content/
./build_product
cd build
ctest -L quick
ctest -LE quick -j4
```

Note: CTest does not run [Automatus](https://github.com/ComplianceAsCode/content/tree/master/tests) which provides simple system of test scenarios for testing profiles and rule remediations.

## Profiling the buildsystem

To make sure your changes don't prolong the time that it takes to build products by using the `build_product` script too much, you can use the `-p|--profiling` switch to get a report containing build times of all build targets/files.
You can compare build times between a baseline profiling log and your current log to see exactly which targets/files are taking longer to build, what percentage of the total build time they take up, and even see what targets you have added/removed and how did that affect the build time.
You also get an interactive HTML report that visualises how much time each target/file takes up.

For details about how this works, see `section 5 - tools and utilities - Profiling the buildsystem`.

## Installation

System-wide installation:

```bash
cd content/
cd build/
cmake ../
make -j4
sudo make install
```

(optional) Custom install location:

```bash
cd content/
cd build/
cmake ../
make -j4
sudo make DESTDIR=/opt/absolute/path/to/ssg/ install
```

(optional) System-wide installation using ninja:

```bash
cd content/
cd build/
cmake -G Ninja ../
ninja-build
ninja-build install
```

## Extra Building Options

### Building a tarball

To build a tarball with all the source code:

```bash
cd build/
make package_source
```

### Building a package

To build a package for testing purposes:

```bash
cd build/
# disable any product you would not like to bundle in the package. For example:
cmake -DSSG_PRODUCT_FEDORA:BOOL=OFF../
# build the package.
make package
```

Currently, RPM and DEB packages are supported by this mechanism. We recommend
only using it for testing. Please follow downstream workflows for production
packages.

#### Use of pip3 packages when building

There may be situations during the development and testing phases where it is
convenient to use Python modules installed via pip3, as in [this example](https://github.com/ComplianceAsCode/content/pull/7376/files),
where the `xmldiff` module is needed for some tests, but it is not available
in the official distro repositories and therefore needs to be installed via pip3.

However, for some time now, Python modules installed via pip3 have been located
in a different path, to reduce the risk of user installed modules conflicting
or even breaking official distro packages that depend on related Python modules.
More information and context can be found [here](https://fedoraproject.org/wiki/Changes/Making_sudo_pip_safe).

The consequence of this is that in some situations, such as during the build
time of an RPM package, modules installed via pip3 are not detected, because in
the context of rpmbuild there is no influence from external commands (pip3).

To work around this in test environments, an OS environment variable was created
to be evaluated by CMake for this purpose. If the OS environment variable
`SSG_USE_PIP_PACKAGES` is set and has a [positive value](https://cmake.org/cmake/help/latest/command/if.html#basic-expressions), CMake will ensure that
the [PYTHONPATH](https://docs.python.org/3/tutorial/modules.html#the-module-search-path) variable is set in the Python context with the proper location
of the python packages installed via pip3.

If `SSG_USE_PIP_PACKAGES` is not set or is set to a negative value (0, Off, No, False, N),
it will simply be ignored by CMake without any effect on the build process.

In the following example, Python modules installed via pip3 will be found
during the RPM build phase, in a test environment:

```bash
export SSG_USE_PIP_PACKAGES=1
rpmbuild -v -bc /root/rpmbuild/SPECS/scap-security-guide.spec
```

### Building a ZIP file

To build a zip file with all generated source data streams and kickstarts:

```bash
cd build/
make zipfile
```

### Build the Docker container image

Find a suitable Dockerfile present in the
[Dockerfiles](https://github.com/ComplianceAsCode/content/tree/master/Dockerfiles)
directory and build the image.
This will take care of the build environment and all necessary setup.

```bash
docker build --no-cache --file Dockerfiles/ubuntu --tag oscap:$(date -u +%Y%m%d%H%M) --tag oscap:latest .
```

### Build the content using the container image

To build all the content, run a container without any flags.

```bash
docker run --cap-drop=all --name oscap-content oscap:latest
```

Using `docker cp` to copy all the generated content to your host:

```bash
docker cp oscap-content:/home/oscap/content/build $(pwd)/container_build
```
