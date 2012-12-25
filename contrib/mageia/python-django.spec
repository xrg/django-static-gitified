%define git_repo python-django
%define git_head HEAD

%define module	django
%define tarname	Django

Summary:	A high-level Python Web framework
Name:		python-%module
Version:	%git_get_ver
Release:	%mkrel %git_get_rel2
Source:		%git_bs_source %{name}-%{version}.tar.gz
Source1:	%{name}-gitrpm.version
Source2:	%{name}-changelog.gitrpm.txt
License:	BSD
Group:		Development/Python
Url:		http://www.djangoproject.com
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:  python-sphinx
BuildRequires:  python-devel

%description
Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design.

Developed and used over the past two years by a fast-moving online-news
operation, Django was designed from scratch to handle two challenges: the
intensive deadlines of a newsroom and the stringent requirements of experienced
Web developers. It has convenient niceties for developing content-management
systems, but it's an excellent tool for building any Web site.

Django focuses on automating as much as possible and adhering to the
DRY principle.

%prep
%git_get_source
%setup -q
sed -i 's/^\(ez_setup.use_setuptools\)/#\1/' setup.py

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build
make -C docs/ html

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%doc LICENSE README docs/_build/html
%_bindir/*
%py_puresitedir/%{module}
%py_puresitedir/%{tarname}-*.egg-info
