%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name: ansible
Release: 1
Summary: Minimal SSH command and control
Version: 0.0.1

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Group: Development/Libraries
License: GPLv3
Prefix: %{_prefix}
Source0: ansible-%{version}.tar.gz
Url: http://ansible.github.com

BuildArch: noarch
BuildRequires: asciidoc
BuildRequires: python-devel

Requires: python-paramiko
Requires: python-jinja2

%description
Ansible is a extra-simple tool/API for doing 'parallel remote things' over SSH
executing commands, running "modules", or executing larger 'playbooks' that
can serve as a configuration management or deployment system.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build
make docs

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mkdir -p $RPM_BUILD_ROOT/etc/ansible/
cp examples/hosts $RPM_BUILD_ROOT/etc/ansible/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md AUTHORS.md PKG-INFO
%defattr(-,root,root)
%{_mandir}/man1/*.gz
%{python_sitelib}/*
%{_bindir}/ansible*
%{_datadir}/ansible/*
%config(noreplace) %{_sysconfdir}/ansible/


%changelog
* Sat Mar 10 2012  <tbielawa@redhat.com> - 0.0.1-1
- Release of 0.0.1
