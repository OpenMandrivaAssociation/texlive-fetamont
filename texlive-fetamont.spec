# revision 33221
# category Package
# catalog-ctan /fonts/fetamont
# catalog-date 2014-03-18 17:58:58 +0100
# catalog-license lppl1.3
# catalog-version 1.3
Name:		texlive-fetamont
Version:	1.3
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
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmb10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmb8.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmb9.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmbc40.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmbco40.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmbo10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmbo8.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmbo9.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmbw10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmbwo10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmc10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmco10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmh10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmh8.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmh9.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmho10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmho8.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmho9.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmhw10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmhwo10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffml10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmlc10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmlco10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmlo10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmlq10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmlqo10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmlw10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmlwo10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmo10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmo8.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmo9.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmr10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmr8.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmr9.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmw10.afm
%{_texmfdistdir}/fonts/afm/public/fetamont/ffmwo10.afm
%{_texmfdistdir}/fonts/map/dvips/fetamont/fetamont.map
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmb10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmb8.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmb9.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmbc40.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmbco40.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmbo10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmbo8.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmbo9.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmbw10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmbwo10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmc10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmco10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmh10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmh8.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmh9.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmho10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmho8.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmho9.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmhw10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmhwo10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffml10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmlc10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmlco10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmlo10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmlq10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmlqo10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmlw10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmlwo10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmo10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmo8.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmo9.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmr10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmr8.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmr9.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmw10.otf
%{_texmfdistdir}/fonts/opentype/public/fetamont/ffmwo10.otf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmb10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmb8.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmb9.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmbase.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmbc40.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmbco40.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmbo10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmbo8.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmbo9.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmbw10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmbwo10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmc10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_A.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_AE.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Aacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Abreve.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Acircumflex.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Adieresis.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Agrave.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Aogonek.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Aring.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Atilde.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_B.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_C.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Cacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ccaron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ccedilla.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_D.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Dcaron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_E.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Eacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ecaron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ecircumflex.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Edieresis.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Egrave.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Eng.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Eogonek.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Eth.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_F.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_G.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Gbreve.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Germandbls.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_H.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_I.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_IJ.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Iacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Icircumflex.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Idieresis.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Idotaccent.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Igrave.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_J.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_K.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_L.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Lacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Lcaron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Lslash.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_M.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_N.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Nacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ncaron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ntilde.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_O.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_OE.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Oacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ocircumflex.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Odieresis.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ograve.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ohungarumlaut.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Oslash.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Otilde.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_P.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Q.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_R.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Racute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Rcaron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_S.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Sacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Scaron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Scedilla.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_T.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Tcaron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Tcedilla.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Thorn.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_U.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Uacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ucircumflex.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Udieresis.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ugrave.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Uhungarumlaut.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Uring.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_V.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_W.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_X.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Y.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Yacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Ydieresis.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Z.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Zacute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Zcaron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_Zdotaccent.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_acute.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_ampersand.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_asciicircum.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_asciitilde.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_asterisk.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_at.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_backslash.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_bar.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_braceleft.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_braceright.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_bracketleft.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_bracketright.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_breve.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_caron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_cedilla.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_circumflex.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_colon.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_comma.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_cwm.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_dash.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_dieresis.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_dollar.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_dotaccent.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_eight.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_emdash.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_endash.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_equal.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_exclam.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_exclamdown.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_ff.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_ffi.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_ffl.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_fi.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_five.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_fl.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_four.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_grave.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_greater.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_guillemotleft.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_guillemotright.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_guilsinglleft.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_guilsinglright.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_hungarumlaut.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_hyphen.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_ijlower.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_less.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_macron.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_nine.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_numbersign.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_ogonek.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_one.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_parenleft.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_parenright.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_percent.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_period.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_perthousandzero.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_plus.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_question.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_questiondown.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_quotedbl.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_quotedblbase.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_quotedblleft.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_quotedblright.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_quoteleft.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_quoteright.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_quotesinglbase.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_ring.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_section.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_semicolon.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_seven.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_six.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_slash.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_sterling.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_three.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_tilde.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_two.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_underscore.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_visiblespace.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmchar_zero.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmco10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmh10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmh8.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmh9.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmho10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmho8.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmho9.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmhw10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmhwo10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffml10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmlc10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmlco10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmlo10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmlq10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmlqo10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmlw10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmlwo10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmo10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmo8.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmo9.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmr10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmr8.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmr9.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmw10.mf
%{_texmfdistdir}/fonts/source/public/fetamont/ffmwo10.mf
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmb8.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmb9.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmbc40.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmbco40.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmbo10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmbo8.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmbo9.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmbw10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmbwo10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmc10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmco10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmh10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmh8.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmh9.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmho10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmho8.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmho9.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmhw10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmhwo10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffml10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmlc10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmlco10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmlo10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmlq10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmlqo10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmlw10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmlwo10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmo10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmo8.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmo9.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmw10.tfm
%{_texmfdistdir}/fonts/tfm/public/fetamont/ffmwo10.tfm
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmb10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmb8.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmb9.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmbc40.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmbco40.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmbo10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmbo8.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmbo9.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmbw10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmbwo10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmc10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmco10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmh10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmh8.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmh9.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmho10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmho8.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmho9.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmhw10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmhwo10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffml10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmlc10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmlco10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmlo10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmlq10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmlqo10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmlw10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmlwo10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmo10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmo8.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmo9.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmr10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmr8.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmr9.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmw10.pfb
%{_texmfdistdir}/fonts/type1/public/fetamont/ffmwo10.pfb
%{_texmfdistdir}/tex/latex/fetamont/T1ffm.fd
%{_texmfdistdir}/tex/latex/fetamont/T1ffmw.fd
%{_texmfdistdir}/tex/latex/fetamont/fetamont.sty
%doc %{_texmfdistdir}/doc/fonts/fetamont/README
%doc %{_texmfdistdir}/doc/fonts/fetamont/fetamont-typeface.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/fetamont/fetamont.dtx
%doc %{_texmfdistdir}/source/fonts/fetamont/fetamont.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
