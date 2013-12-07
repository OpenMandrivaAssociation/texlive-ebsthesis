# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ebsthesis
# catalog-date 2007-01-07 11:02:17 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-ebsthesis
Version:	1.0
Release:	5
Summary:	Typesetting theses for economics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ebsthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebsthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebsthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebsthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The ebsthesis class and ebstools package facilitate the
production of camera-ready manuscripts in conformance with the
guidelines of Gabler Verlag and typographical rules established
by the European Business School.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ebsthesis/ebsthesis.cls
%doc %{_texmfdistdir}/doc/latex/ebsthesis/README
%doc %{_texmfdistdir}/doc/latex/ebsthesis/ebsthesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ebsthesis/ebsthesis.dtx
%doc %{_texmfdistdir}/source/latex/ebsthesis/ebsthesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751285
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718297
- texlive-ebsthesis
- texlive-ebsthesis
- texlive-ebsthesis
- texlive-ebsthesis

