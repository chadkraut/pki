Name:           pki-native-tools
Version:        9.0.0
Release:        1%{?dist}
Summary:        Dogtag Certificate System - Native Tools
URL:            http://pki.fedoraproject.org/
License:        GPLv2
Group:          System Environment/Base

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cyrus-sasl-devel
BuildRequires:  openldap-devel
BuildRequires:  nspr-devel >= 4.6.99
BuildRequires:  nss-devel >= 3.12.3.99
BuildRequires:  svrcore-devel

Requires:       openldap-clients
Requires:       nss >= 3.12.3.99
Requires:       nss-tools >= 3.12.3.99

Source0:        http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}.tar.gz

%description
Dogtag Certificate System is an enterprise software system designed
to manage enterprise Public Key Infrastructure (PKI) deployments.

These platform-dependent PKI executables are used to help make
Dogtag Certificate System into a more complete and robust PKI solution.

%prep

%setup -q -n %{name}-%{version}

%build
%configure \
%ifarch ppc64 s390x sparc64 x86_64
    --enable-64bit \
%endif
    --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

## rearrange files to be in the desired native packaging layout
mkdir -p %{buildroot}%{_libdir}/pki/native-tools
cp -p %{buildroot}/opt/conf/*      %{buildroot}%{_libdir}/pki/native-tools
cp -p %{buildroot}/opt/samples/*   %{buildroot}%{_libdir}/pki/native-tools
cp -p %{buildroot}%{_libexecdir}/* %{buildroot}%{_libdir}/pki/native-tools

# create wrappers
for wrapper in bulkissuance p7tool revoker setpin sslget tkstool
do
    sed -e "s|\[PKI_PRODUCT\]|pki|g"            \
        -e "s|\[PKI_SUBSYSTEM\]|native-tools|g" \
        -e "s|\[PKI_COMMAND\]|${wrapper}|g" \
        %{buildroot}/opt/templates/pki_subsystem_command_wrapper > %{buildroot}%{_bindir}/${wrapper} ;
done

## remove unwanted files
rm -rf %{buildroot}/opt
rm -rf %{buildroot}%{_libexecdir}
rm -rf %{buildroot}%{_datadir}/pki

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE doc/README
%{_bindir}/*
%{_libdir}/pki

%changelog
* Fri Nov 19 2010 Matthew Harmsen <mharmsen@redhat.com> 9.0.0-1
- Updated Dogtag 1.3.x --> Dogtag 2.0.0 --> Dogtag 9.0.0.

* Thu Nov 18 2010 Ade Lee <alee@redhat.com> 2.0.0-2
- Bugzilla BZ606946 - Convert Native Tools to use ldapAPI from OpenLDAP instead of Mozldap
