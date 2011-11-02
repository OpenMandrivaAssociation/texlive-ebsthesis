Name:		texlive-ebsthesis
Version:	1.0
Release:	1
Summary:	Typesetting theses for economics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ebsthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebsthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebsthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebsthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The ebsthesis class and ebstools package facilitate the
production of camera-ready manuscripts in conformance with the
guidelines of Gabler Verlag and typographical rules established
by the European Business School.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
