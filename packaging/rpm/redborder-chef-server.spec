Name: redborder-chef-server
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Redborder package containing chef-server files

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-chef-server
Source0: %{name}-%{version}.tar.gz

BuildRequires: systemd

Requires: bash chef-server-core

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/usr/lib/redborder/bin
install -D -m 0755 resources/bin/rb_postgresql_start.sh %{buildroot}/usr/lib/redborder/bin/rb_postgresql_start.sh
install -D -m 0755 resources/bin/rb_nginx_start.sh %{buildroot}/usr/lib/redborder/bin/rb_nginx_start.sh
install -D -m 0644 resources/systemd/postgresql.service %{buildroot}/usr/lib/systemd/system/postgresql.service
install -D -m 0644 resources/systemd/nginx.service %{buildroot}/usr/lib/systemd/system/nginx.service
ln -s /usr/lib/systemd/system/private_chef-runsvdir-start.service /usr/lib/systemd/system/chef-server.service

%files
%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_postgresql_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/postgresql.service
%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_nginx_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/nginx.service

%post
%systemd_post postgresql.service
%systemd_post nginx.service
%systemd_post chef-server.service

%changelog
* Fri Sep 02 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-1
- first spec version
