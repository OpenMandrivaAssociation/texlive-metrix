Name:		texlive-metrix
Version:	52323
Release:	2
Summary:	Typeset metric marks for Latin text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/metrix
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metrix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metrix.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metrix.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package may be used to type the prosodics/metrics of
(latin) verse; it provides macros to typeset the symbols
standing alone, and in combination with symbols, giving
automatic alignment. The package requires tikz (including the
calc library, and the xparse package (thus also requiring the
experimental LaTeX 3 environment).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/metrix/metrix.sty
%doc %{_texmfdistdir}/doc/latex/metrix/README
%doc %{_texmfdistdir}/doc/latex/metrix/metrix.pdf
#- source
%doc %{_texmfdistdir}/source/latex/metrix/metrix.dtx
%doc %{_texmfdistdir}/source/latex/metrix/metrix.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
