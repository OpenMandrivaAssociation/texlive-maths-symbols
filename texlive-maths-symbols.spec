%global tl_name maths-symbols
%global tl_revision 37763

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.4
Release:	%{tl_revision}.1
Summary:	Summary of mathematical symbols available in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/symbols/math
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/maths-symbols.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/maths-symbols.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A predecessor of the comprehensive symbols list, covering mathematical
symbols available in standard LaTeX (including the AMS symbols, if
available at compile time).

