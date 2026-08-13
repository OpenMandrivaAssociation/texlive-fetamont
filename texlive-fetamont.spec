%global tl_name fetamont
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Extended version of Knuths logo typeface
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fetamont
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fetamont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fetamont.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fetamont.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The fetamont typeface was designed in Metafont and extends the Logo
fonts to complete the T1 encoding. The designs of the glyphs A, E, F, M,
N, O, P, S and T are based on the Metafont constructions by D. E. Knuth.
The glyphs Y and 1 imitate the shapes of the corresponding glyphs in the
METATYPE1 logo.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from fetamont:
Map fetamont.map
TL_DROPIN_EOF
