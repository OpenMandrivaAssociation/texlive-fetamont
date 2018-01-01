Name:		texlive-fetamont
Version:	20170415
Release:	1
Summary:	Extended version of Knuth's logo typeface
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fetamont
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fetamont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fetamont.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fetamont.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
