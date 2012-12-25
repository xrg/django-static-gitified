%define module	django
%define tarname	Django
%define name	python-%module
%define version	1.4.3
%define release	%mkrel 1

Summary:	A high-level Python Web framework
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.djangoproject.com/m/releases/1.4/Django-%{version}.tar.gz
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
%setup -q -n %{tarname}-%{version}
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
