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
install -D -m 0755 resources/bin/rb_bookshelf_start.sh %{buildroot}/usr/lib/redborder/bin/rb_bookshelf_start.sh
install -D -m 0755 resources/bin/rb_oc_bifrost_start.sh %{buildroot}/usr/lib/redborder/bin/rb_oc_bifrost_start.sh
install -D -m 0755 resources/bin/rb_oc_id_start.sh %{buildroot}/usr/lib/redborder/bin/rb_oc_id_start.sh
install -D -m 0755 resources/bin/rb_opscode-erchef_start.sh %{buildroot}/usr/lib/redborder/bin/rb_opscode-erchef_start.sh
install -D -m 0755 resources/bin/rb_redis_lb_start.sh %{buildroot}/usr/lib/redborder/bin/rb_redis_lb_start.sh
install -D -m 0755 resources/bin/rb_opensearch_start.sh %{buildroot}/usr/lib/redborder/bin/rb_opensearch_start.sh
install -D -m 0755 resources/bin/rb_chef-server_start.sh %{buildroot}/usr/lib/redborder/bin/rb_chef-server_start.sh
install -D -m 0644 resources/systemd/opscode-postgresql.service %{buildroot}/usr/lib/systemd/system/opscode-postgresql.service
install -D -m 0644 resources/systemd/opscode-nginx.service %{buildroot}/usr/lib/systemd/system/opscode-nginx.service
install -D -m 0644 resources/systemd/opscode-bookshelf.service %{buildroot}/usr/lib/systemd/system/opscode-bookshelf.service
install -D -m 0644 resources/systemd/opscode-oc_bifrost.service %{buildroot}/usr/lib/systemd/system/opscode-oc_bifrost.service
install -D -m 0644 resources/systemd/opscode-oc_id.service %{buildroot}/usr/lib/systemd/system/opscode-oc_id.service
install -D -m 0644 resources/systemd/opscode-erchef.service %{buildroot}/usr/lib/systemd/system/opscode-erchef.service
install -D -m 0644 resources/systemd/opscode-redis_lb.service %{buildroot}/usr/lib/systemd/system/opscode-redis_lb.service
install -D -m 0644 resources/systemd/opscode-opensearch.service %{buildroot}/usr/lib/systemd/system/opscode-opensearch.service

%files
%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_postgresql_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-postgresql.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_nginx_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-nginx.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_bookshelf_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-bookshelf.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_oc_bifrost_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-oc_bifrost.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_oc_id_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-oc_id.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_opscode-erchef_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-erchef.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_redis_lb_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-redis_lb.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_opensearch_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-opensearch.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_chef-server_start.sh

%post
#%systemd_post opscode-postgresql.service
%systemd_post opscode-nginx.service
%systemd_post opscode-bookshelf.service
%systemd_post opscode-oc_bifrost.service
%systemd_post opscode-oc_id.service
%systemd_post opscode-erchef.service
%systemd_post opscode-redis_lb.service
%systemd_post opscode-opensearch.service

%changelog
* Fri Oct 13 2023 Miguel Negrón <manegron@redborder.com>
- Update chef 15

* Fri Nov 04 2016 Carlos J. Mateos <cjmateos@redborder.com> 1.0.0-14
- Rename chef-server unit files

* Mon Sep 26 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-13
- Added path to opscode-erchef aswell

* Fri Sep 23 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-12
- Add path to all scripts

* Thu Sep 22 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-11
- Add opscode path to rabbitmq init script

* Wed Sep 21 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-10
- Fix init scripts call

* Wed Sep 21 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-9
- Fix wrong variable definition on oc_id init scipt

* Wed Sep 21 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-8
- Run postgresql init script with opscode-pgsql instead opscode user

* Wed Sep 21 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-7
- Run nginx init script with root instead opscode user

* Tue Sep 20 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-6
- Fix typo on nginx unit file

* Tue Sep 20 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-5
- Add user to unit file instead init script

* Mon Sep 19 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-4
- Replace runit to systemd

* Mon Sep 12 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-3
- Fix typo on opscode-erchef unit file

* Fri Sep 02 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-2
- Add separated systemd unit file for chef

* Fri Sep 02 2016 Enrique Jimenez <ejimenez@redborder.com> 1.0.0-1
- first spec version
