%{!?_version: %define _version 1 }
%{!?_release: %define _release 0 }

Name: nvme-dem
Version: %{_version}
Release: %{_release}%{?dist}
Summary: NVMe over Fabrics Distributed Endpoint Management suite

Group: User-mode Administrative Tools
License: GPLv2 or BSD
Url: http://www.github.com/linux-nvme/%{name}
Source: http://www.github.com/linux-nvme/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
NVMe over Fabrics (NVMe-oF) Distributed Endpoint Management (dem) is an
implementation of a centralized Discovery controller providing remote
configuration and provisioning of remote NVMe resources.

%prep
%setup -q -n %{name}-%{version}

%build
./autoconf.sh
%configure %{configopts}
make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir /etc/nvme/
%{_prefix}/local/share/bash_completion.d/dem-cli
%{_bindir}/dem-cli
%{_bindir}/dem-dm
%{_bindir}/dem-em
%{_bindir}/dem-ac
%{_bindir}/dem
%{_sysconfdir}/nvme/nvmeof.conf
%{_sysconfdir}/nvme/nvmeof-dem
%{_libexecdir}/nvmeof
%{_prefix}/lib/systemd/system/nvmeof.service
%{_mandir}/man1/dem-cli.1.gz
%{_mandir}/man1/dem-dm.1.gz
%{_mandir}/man8/dem-em.8.gz
%{_mandir}/man8/dem-ac.8.gz
%{_mandir}/man8/dem.8.gz
%doc AUTHORS COPYING README

%changelog
2019-04-22 created spec file
