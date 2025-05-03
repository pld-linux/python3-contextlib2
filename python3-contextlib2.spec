#
# Conditional build:
%bcond_without	tests	# test target

Summary:	Backports and enhancements for the contextlib module
Summary(pl.UTF-8):	Backport oraz rozszerzenia dla modułu contextlib
Name:		python3-contextlib2
Version:	21.6.0
Release:	1
License:	PSF
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/contextlib2/
Source0:	https://files.pythonhosted.org/packages/source/c/contextlib2/contextlib2-%{version}.tar.gz
# Source0-md5:	dcdca610617ab7fffc6fd99665567987
URL:		https://contextlib2.readthedocs.io/
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
contextlib2 is a backport of the `standard library's contextlib module
<https://docs.python.org/3.5/library/contextlib.html> to earlier
Python versions.

contextlib module provides utilities for with-statement contexts.

%description -l pl.UTF-8
contextlib2 to backport modułu contextlib z biblioteki standardowej
(<https://docs.python.org/3.5/library/contextlib.html>) do starszych
wersji Pythona.

Moduł contextlib udostępnia narzędzia dla kontekstów ustalanych
instrukcją with.

%prep
%setup -q -n contextlib2-%{version}

%build
%py3_build

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt NEWS.rst README.rst
%{py3_sitescriptdir}/contextlib2
%{py3_sitescriptdir}/contextlib2-%{version}-py*.egg-info
