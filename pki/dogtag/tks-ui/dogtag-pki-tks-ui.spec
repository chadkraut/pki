Name:           dogtag-pki-tks-ui
Version:        9.0.0
Release:        1%{?dist}
Summary:        Dogtag Certificate System - Token Key Service User Interface
URL:            http://pki.fedoraproject.org/
License:        GPLv2
Group:          System Environment/Base

BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ant

Source0:        http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}.tar.gz

# NOTE:  Several PKI packages require a "virtual" UI component.  These
#        "virtual" UI components are "Provided" by various UI "flavors"
#        including "dogtag", "redhat", and "null".  Consequently,
#        all "dogtag", "redhat", and "null" UI components MUST be
#        mutually exclusive!
Provides:       pki-tks-ui = %{version}-%{release}

Obsoletes:      pki-tks-ui < %{version}-%{release}

Conflicts:      redhat-pki-tks-ui

%description
Dogtag Certificate System is an enterprise software system designed
to manage enterprise Public Key Infrastructure (PKI) deployments.

The Dogtag Token Key Service User Interface contains the graphical
user interface for the Dogtag Token Key Service.

%prep

%setup -q

%build
ant \
    -Dproduct.ui.flavor.prefix="dogtag" \
    -Dproduct.prefix="pki" \
    -Dproduct="tks-ui" \
    -Dversion="%{version}"

%install
rm -rf %{buildroot}
cd dist/binary
unzip %{name}-%{version}.zip -d %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_datadir}/pki/

%changelog
* Fri Nov 19 2010 Matthew Harmsen <mharmsen@redhat.com> 9.0.0-1
- Updated Dogtag 1.3.x --> Dogtag 2.0.0 --> Dogtag 9.0.0.
