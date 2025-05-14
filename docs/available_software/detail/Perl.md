---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Larry Wall's Practical Extraction and Report LanguageIncludes a small
    selection of extra CPAN packages for core functionality.
  license: Not confirmed
  name: Perl
  offers:
    '@type': Offer
    price: 0
  operatingSystem: LINUX
  review:
    '@type': Review
    author:
      '@type': Organization
      name: EESSI
    reviewBody: Application has been successfully made available on all architectures
      supported by EESSI
    reviewRating:
      '@type': Rating
      ratingValue: 5
  softwareRequirements: See https://www.eessi.io/docs/ for how to make EESSI available
    on your system
  softwareVersion: '[''Perl/5.36.0-GCCcore-12.2.0'', ''Perl/5.36.0-GCCcore-12.2.0-minimal'',
    ''Perl/5.36.1-GCCcore-12.3.0'', ''Perl/5.38.0-GCCcore-13.2.0'']'
  url: https://www.perl.org/
---

Perl
====


Larry Wall's Practical Extraction and Report LanguageIncludes a small selection of extra CPAN packages for core functionality.

https://www.perl.org/
# Available modules


The overview below shows which Perl installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Perl, load one of these modules using a `module load` command like:

```shell
module load Perl/5.38.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Perl/5.38.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|Perl/5.36.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|Perl/5.36.0-GCCcore-12.2.0-minimal|x|x|x|x|x|x|x|x|x|x|x|
|Perl/5.36.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|


### Perl/5.38.0-GCCcore-13.2.0

This is a list of extensions included in the module:

Carp-1.50, constant-1.33, Data::Dumper-2.183, Exporter-5.77, File::Path-2.18, File::Spec-3.75, Getopt::Long-2.54, IO::File-1.51, Text::ParseWords-3.31, Thread::Queue-3.13, threads-2.21

### Perl/5.36.1-GCCcore-12.3.0

This is a list of extensions included in the module:

Carp-1.50, constant-1.33, Data::Dumper-2.183, Exporter-5.77, File::Path-2.18, File::Spec-3.75, Getopt::Long-2.54, IO::File-1.51, Text::ParseWords-3.31, Thread::Queue-3.13, threads-2.21

### Perl/5.36.0-GCCcore-12.2.0

This is a list of extensions included in the module:

Algorithm::Dependency-1.112, Algorithm::Diff-1.201, aliased-0.34, AnyEvent-7.17, App::Cmd-0.334, App::cpanminus-1.7046, AppConfig-1.71, Archive::Extract-0.88, Array::Transpose-0.06, Array::Utils-0.5, Authen::NTLM-1.09, Authen::SASL-2.16, AutoLoader-5.74, B::Hooks::EndOfScope-0.26, B::Lint-1.20, boolean-0.46, Business::ISBN-3.007, Business::ISBN::Data-20210112.006, Canary::Stability-2013, Capture::Tiny-0.48, Carp-1.50, Carp::Clan-6.08, Carp::Heavy-1.50, Class::Accessor-0.51, Class::Data::Inheritable-0.09, Class::DBI-v3.0.17, Class::DBI::SQLite-0.11, Class::Inspector-1.36, Class::ISA-0.36, Class::Load-0.25, Class::Load::XS-0.10, Class::Singleton-1.6, Class::Tiny-1.008, Class::Trigger-0.15, Clone-0.45, Clone::Choose-0.010, common::sense-3.75, Config::General-2.65, Config::INI-0.027, Config::MVP-2.200012, Config::Simple-4.58, Config::Tiny-2.28, constant-1.33, CPAN::Meta::Check-0.014, CPANPLUS-0.9914, Crypt::DES-2.07, Crypt::Rijndael-1.16, Cwd-3.75, Cwd::Guard-0.05, Data::Dump-1.25, Data::Dumper-2.183, Data::Dumper::Concise-2.023, Data::Grove-0.08, Data::OptList-0.112, Data::Section-0.200007, Data::Section::Simple-0.07, Data::Stag-0.14, Data::Types-0.17, Data::UUID-1.226, Date::Handler-1.2, Date::Language-2.33, DateTime-1.58, DateTime::Locale-1.36, DateTime::TimeZone-2.53, DateTime::Tiny-1.07, DBD::CSV-0.59, DBD::SQLite-1.70, DBI-1.643, DBIx::Admin::TableInfo-3.04, DBIx::ContextualFetch-1.03, DBIx::Simple-1.37, Devel::CheckCompiler-0.07, Devel::CheckLib-1.16, Devel::Cycle-1.12, Devel::GlobalDestruction-0.14, Devel::OverloadInfo-0.007, Devel::Size-0.83, Devel::StackTrace-2.04, Digest::HMAC-1.04, Digest::MD5::File-0.08, Digest::SHA1-2.13, Dist::CheckConflicts-0.11, Dist::Zilla-6.025, Email::Date::Format-1.005, Encode-3.19, Encode::Locale-1.05, Error-0.17029, Eval::Closure-0.14, Exception::Class-1.45, Expect-1.35, Exporter-5.74, Exporter::Declare-0.114, Exporter::Tiny-1.004000, ExtUtils::CBuilder-0.280236, ExtUtils::Config-0.008, ExtUtils::Constant-0.25, ExtUtils::CppGuess-0.26, ExtUtils::Helpers-0.026, ExtUtils::InstallPaths-0.012, ExtUtils::MakeMaker-7.64, ExtUtils::ParseXS-3.44, Fennec::Lite-0.004, File::CheckTree-4.42, File::Copy::Recursive-0.45, File::Copy::Recursive::Reduced-0.006, File::Find::Rule-0.34, File::Find::Rule::Perl-1.16, File::Grep-0.02, File::HomeDir-1.006, File::Listing-6.15, File::Next-1.18, File::Path-2.18, File::pushd-1.016, File::Remove-1.61, File::ShareDir-1.118, File::ShareDir::Install-0.14, File::Slurp-9999.32, File::Slurp::Tiny-0.004, File::Slurper-0.013, File::Spec-3.75, File::Temp-0.2311, File::Which-1.27, Font::TTF-1.06, Getopt::Long-2.52, Getopt::Long::Descriptive-0.110, Git-0.42, GO-0.04, GO::Utils-0.15, Graph-0.9725, Graph::ReadWrite-2.10, Hash::Merge-0.302, Heap-0.80, HTML::Entities::Interpolate-1.10, HTML::Form-6.10, HTML::Parser-3.78, HTML::Tagset-3.20, HTML::Template-2.97, HTML::Tree-5.07, HTTP::Cookies-6.10, HTTP::Daemon-6.14, HTTP::Date-6.05, HTTP::Negotiate-6.01, HTTP::Request-6.37, HTTP::Tiny-0.082, if-0.0608, Ima::DBI-0.35, Import::Into-1.002005, Importer-0.026, Inline-0.86, IO::HTML-1.004, IO::Socket::SSL-2.075, IO::String-1.08, IO::Stringy-2.113, IO::Tty-1.16, IPC::Cmd-1.04, IPC::Run-20220807.0, IPC::Run3-0.048, IPC::System::Simple-1.30, JSON-4.09, JSON::XS-4.03, Lingua::EN::PluralToSingular-0.21, List::AllUtils-0.19, List::MoreUtils-0.430, List::MoreUtils::XS-0.430, List::SomeUtils-0.58, List::Util-1.63, List::UtilsBy-0.12, local::lib-2.000029, Locale::Maketext::Simple-0.21, Log::Dispatch-2.70, Log::Dispatchouli-2.023, Log::Handler-0.90, Log::Log4perl-1.56, Log::Message-0.08, Log::Message::Simple-0.10, Log::Report-1.33, Log::Report::Optional-1.07, Logger::Simple-2.0, LWP::MediaTypes-6.04, LWP::Protocol::https-6.10, LWP::Simple-6.67, Mail::Util-2.21, Math::Bezier-0.01, Math::CDF-0.1, Math::Round-0.07, Math::Utils-1.14, Math::VecStat-0.08, MCE::Mutex-1.879, Meta::Builder-0.004, MIME::Base64-3.16, MIME::Charset-1.013.1, MIME::Lite-3.033, MIME::Types-2.22, Mixin::Linewise::Readers-0.110, Mock::Quick-1.111, Module::Build-0.4231, Module::Build::Tiny-0.039, Module::Build::XSUtil-0.19, Module::CoreList-5.20220820, Module::Implementation-0.09, Module::Install-1.19, Module::Load-0.36, Module::Load::Conditional-0.74, Module::Metadata-1.000037, Module::Path-0.19, Module::Pluggable-5.2, Module::Runtime-0.016, Module::Runtime::Conflicts-0.003, Moo-2.005004, Moose-2.2201, MooseX::LazyRequire-0.11, MooseX::OneArgNew-0.006, MooseX::Role::Parameterized-1.11, MooseX::SetOnce-0.201, MooseX::Types-0.50, MooseX::Types::Perl-0.101343, Mouse-v2.5.10, Mozilla::CA-20211001, MRO::Compat-0.15, namespace::autoclean-0.29, namespace::clean-0.27, Net::Domain-3.14, Net::HTTP-6.22, Net::SMTP::SSL-1.04, Net::SNMP-v6.0.1, Net::SSLeay-1.92, Number::Compare-0.03, Number::Format-1.75, Object::Accessor-0.48, Object::InsideOut-4.05, Package::Constants-0.06, Package::DeprecationManager-0.17, Package::Stash-0.40, Package::Stash::XS-0.30, PadWalker-2.5, Parallel::ForkManager-2.02, Params::Check-0.38, Params::Util-1.102, Params::Validate-1.30, Params::ValidationCompiler-0.30, parent-0.238, Parse::RecDescent-1.967015, Path::Tiny-0.124, PDF::API2-2.043, Perl::OSType-1.010, PerlIO::utf8_strict-0.009, Pod::Elemental-0.103005, Pod::Escapes-1.07, Pod::Eventual-0.094002, Pod::LaTeX-0.61, Pod::Man-4.14, Pod::Parser-1.66, Pod::Plainer-1.04, Pod::POM-2.01, Pod::Simple-3.43, Pod::Weaver-4.018, Readonly-2.05, Regexp::Common-2017060201, Role::HasMessage-0.006, Role::Identifiable::HasIdent-0.008, Role::Tiny-2.002004, Scalar::Util-1.63, Scalar::Util::Numeric-0.40, Scope::Guard-0.21, Set::Array-0.30, Set::IntervalTree-0.12, Set::IntSpan-1.19, Set::IntSpan::Fast-1.15, Set::Object-1.42, Set::Scalar-1.29, Shell-0.73, Socket-2.036, Software::License-0.104002, Specio-0.48, SQL::Abstract-2.000001, SQL::Statement-1.414, Statistics::Basic-1.6611, Statistics::Descriptive-3.0800, Storable-3.25, strictures-2.000006, String::Flogger-1.101245, String::Print-0.94, String::RewritePrefix-0.008, String::Truncate-1.100602, Sub::Exporter-0.988, Sub::Exporter::ForMethods-0.100054, Sub::Exporter::Progressive-0.001013, Sub::Identify-0.14, Sub::Info-0.002, Sub::Install-0.928, Sub::Name-0.26, Sub::Quote-2.006006, Sub::Uplevel-0.2800, Sub::Uplevel-0.2800, SVG-2.87, Switch-2.17, Sys::Info-0.7811, Sys::Info::Base-0.7807, Sys::Info::Driver::Linux-0.7905, Sys::Info::Driver::Unknown-0.79, Template-3.101, Template::Plugin::Number::Format-1.06, Term::Encoding-0.03, Term::ReadKey-2.38, Term::ReadLine::Gnu-1.42, Term::Table-0.016, Term::UI-0.50, Test-1.26, Test2::Plugin::NoWarnings-0.09, Test2::Require::Module-0.000145, Test::ClassAPI-1.07, Test::CleanNamespaces-0.24, Test::Deep-1.130, Test::Differences-0.69, Test::Exception-0.43, Test::Fatal-0.016, Test::File::ShareDir::Dist-1.001002, Test::Harness-3.44, Test::LeakTrace-0.17, Test::Memory::Cycle-1.06, Test::More-1.302191, Test::More::UTF8-0.05, Test::Most-0.37, Test::Needs-0.002009, Test::NoWarnings-1.06, Test::Output-1.033, Test::Pod-1.52, Test::Requires-0.11, Test::RequiresInternet-0.05, Test::Simple-1.302191, Test::Version-2.09, Test::Warn-0.37, Test::Warnings-0.031, Test::Without::Module-0.20, Text::Aligner-0.16, Text::Balanced-2.06, Text::CSV-2.02, Text::CSV_XS-1.48, Text::Diff-1.45, Text::Format-0.62, Text::Glob-0.11, Text::Iconv-1.7, Text::ParseWords-3.31, Text::Soundex-3.05, Text::Table-1.134, Text::Template-1.61, Thread::Queue-3.13, Throwable-1.000, Tie::Function-0.02, Tie::IxHash-1.23, Time::HiRes-1.9764, Time::Local-1.30, Time::Piece-1.3401, Time::Piece::MySQL-0.06, Tree::DAG_Node-1.32, Try::Tiny-0.31, Types::Serialiser-1.01, Unicode::LineBreak-2019.001, UNIVERSAL::moniker-0.08, Unix::Processors-2.046, URI-5.12, URI::Escape-5.12, Variable::Magic-0.62, version-0.9929, Want-0.29, WWW::RobotRules-6.02, XML::Bare-0.53, XML::DOM-1.46, XML::Filter::BufferText-1.01, XML::NamespaceSupport-1.12, XML::Parser-2.46, XML::RegExp-0.04, XML::SAX-1.02, XML::SAX::Base-1.09, XML::SAX::Expat-0.51, XML::SAX::Writer-0.57, XML::Simple-2.25, XML::Tiny-2.07, XML::Twig-3.52, XML::XPath-1.48, XSLoader-0.24, YAML-1.30, YAML::Tiny-1.73