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
install -D -m 0755 resources/bin/rb_opscode-chef-mover_start.sh %{buildroot}/usr/lib/redborder/bin/rb_opscode-chef-mover_start.sh
install -D -m 0755 resources/bin/rb_opscode-erchef_start.sh %{buildroot}/usr/lib/redborder/bin/rb_opscode-erchef_start.sh
install -D -m 0755 resources/bin/rb_opscode-expander_start.sh %{buildroot}/usr/lib/redborder/bin/rb_opscode-expander_start.sh
install -D -m 0755 resources/bin/rb_opscode-solr4_start.sh %{buildroot}/usr/lib/redborder/bin/rb_opscode-solr4_start.sh
install -D -m 0755 resources/bin/rb_rabbitmq_start.sh %{buildroot}/usr/lib/redborder/bin/rb_rabbitmq_start.sh
install -D -m 0755 resources/bin/rb_redis_lb_start.sh %{buildroot}/usr/lib/redborder/bin/rb_redis_lb_start.sh
install -D -m 0755 resources/bin/rb_chef-server_start.sh %{buildroot}/usr/lib/redborder/bin/rb_chef-server_start.sh
install -D -m 0644 resources/systemd/postgresql.service %{buildroot}/usr/lib/systemd/system/postgresql.service
install -D -m 0644 resources/systemd/nginx.service %{buildroot}/usr/lib/systemd/system/nginx.service
install -D -m 0644 resources/systemd/bookshelf.service %{buildroot}/usr/lib/systemd/system/bookshelf.service
install -D -m 0644 resources/systemd/oc_bifrost.service %{buildroot}/usr/lib/systemd/system/oc_bifrost.service
install -D -m 0644 resources/systemd/oc_id.service %{buildroot}/usr/lib/systemd/system/oc_id.service
install -D -m 0644 resources/systemd/opscode-chef-mover.service %{buildroot}/usr/lib/systemd/system/opscode-chef-mover.service
install -D -m 0644 resources/systemd/opscode-erchef.service %{buildroot}/usr/lib/systemd/system/opscode-erchef.service
install -D -m 0644 resources/systemd/opscode-expander.service %{buildroot}/usr/lib/systemd/system/opscode-expander.service
install -D -m 0644 resources/systemd/opscode-solr4.service %{buildroot}/usr/lib/systemd/system/opscode-solr4.service
install -D -m 0644 resources/systemd/rabbitmq.service %{buildroot}/usr/lib/systemd/system/rabbitmq.service
install -D -m 0644 resources/systemd/redis_lb.service %{buildroot}/usr/lib/systemd/system/redis_lb.service

%files
%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_postgresql_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/postgresql.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_nginx_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/nginx.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_bookshelf_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/bookshelf.service


%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_oc_bifrost_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/oc_bifrost.service


%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_oc_id_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/oc_id.service


%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_opscode-chef-mover_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-chef-mover.service


%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_opscode-erchef_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-erchef.service


%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_opscode-expander_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-expander.service


%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_opscode-solr4_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/opscode-solr4.service


%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_rabbitmq_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/rabbitmq.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_redis_lb_start.sh
%defattr(0644,root,root)
/usr/lib/systemd/system/redis_lb.service

%defattr(0755,root,root)
/usr/lib/redborder/bin/rb_chef-server_start.sh

%post
%systemd_post postgresql.service
%systemd_post nginx.service
%systemd_post bookshelf.service
%systemd_post oc_bifrost.service
%systemd_post oc_id.service
%systemd_post opscode-chef-mover.service
%systemd_post opscode-erchef.service
%systemd_post opscode-expander.service
%systemd_post opscode-solr4.service
%systemd_post rabbitmq.service
%systemd_post redis_lb.service

%changelog
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
