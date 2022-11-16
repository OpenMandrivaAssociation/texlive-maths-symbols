Name:		texlive-maths-symbols
Version:	37763
Release:	1
Summary:	Summary of mathematical symbols available in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/maths-symbols
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/maths-symbols.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/maths-symbols.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A predecessor of the comprehensive symbols list, covering
mathematical symbols available in standard LaTeX (including the
AMS symbols, if available at compile time).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/maths-symbols

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
