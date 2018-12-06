# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/events
%global commit          6abd29112cdf75ad0172e0df89764bf3a9b7a5c7

%global common_description %{expand:
Events service definition for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Events service definition for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/google/go-github/github)
BuildRequires: golang(github.com/shurcooL/githubql)
BuildRequires: golang(github.com/shurcooL/users)
BuildRequires: golang(github.com/shurcooL/webdavfs/vfsutil)
BuildRequires: golang(golang.org/x/net/webdav)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git6abd291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420git6abd291
- First package for Fedora

