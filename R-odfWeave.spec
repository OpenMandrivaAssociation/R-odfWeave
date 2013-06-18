%global packname  odfWeave
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          0.8.2
Release:          2
Summary:          Sweave processing of Open Document Format (ODF) files
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/odfWeave_0.8.2.tar.gz
Requires:         R-lattice R-XML 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-lattice R-XML

%description
Sweave processing of Open Document Format (ODF) files

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME
# Opening and ending tag mismatch: list-style line 132 and list-level-style-bullet
# Opening and ending tag mismatch: automatic-styles line 13 and list-level-style-bullet
# Opening and ending tag mismatch: document-content line 2 and list-level-style-bullet
# Extra content at the end of the document
# Error: 1: Opening and ending tag mismatch: list-style line 132 and list-level-style-bullet
# 2: Opening and ending tag mismatch: automatic-styles line 13 and list-level-style-bullet
# 3: Opening and ending tag mismatch: document-content line 2 and list-level-style-bullet
# 4: Extra content at the end of the document
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/validate
