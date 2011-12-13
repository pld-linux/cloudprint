Summary:	Google Cloudprint Proxy
Name:		cloudprint
Version:	0.5
Release:	1
License:	GPL v3
Group:		Development/Languages/Python
Source0:	https://github.com/armooo/cloudprint/tarball/master#/%{name}.tgz
# Source0-md5:	b2a161dab9a385d696472e03632d267f
URL:		https://github.com/armooo/cloudprint
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	python-pycups
Suggests:	python-daemon
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Share your CUPS printers with Google Cloud Print.

%prep
%setup -qc
mv *-%{name}-*/* .

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}-%{version}*.egg-info
