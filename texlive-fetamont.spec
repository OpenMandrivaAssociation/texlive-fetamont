Name:		texlive-fetamont
Version:	43812
Release:	2
Summary:	Extended version of Knuth's logo typeface
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fetamont
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fetamont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fetamont.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fetamont.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fetamont typeface was designed in METAFONT and extends the
Logo fonts to complete the T1 encoding. The designs of the
glyphs A, E, F, M, N, O, P, S and T are based on the METAFONT
constructions by D. E. Knuth. The glyphs Y and 1 imitate the
shapes of the corresponding glyphs in the METATYPE1 logo.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/fetamont
%{_texmfdistdir}/fonts/map/dvips/fetamont
%{_texmfdistdir}/fonts/opentype/public/fetamont
%{_texmfdistdir}/fonts/source/public/fetamont
%{_texmfdistdir}/fonts/tfm/public/fetamont
%{_texmfdistdir}/fonts/type1/public/fetamont
%{_texmfdistdir}/tex/latex/fetamont
%doc %{_texmfdistdir}/doc/fonts/fetamont
#- source
%doc %{_texmfdistdir}/source/fonts/fetamont

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
