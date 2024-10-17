Name:		texlive-ebsthesis
Version:	15878
Release:	2
Summary:	Typesetting theses for economics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ebsthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebsthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebsthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebsthesis.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
