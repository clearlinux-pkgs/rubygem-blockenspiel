#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-blockenspiel
Version  : 0.5.0
Release  : 9
URL      : https://rubygems.org/downloads/blockenspiel-0.5.0.gem
Source0  : https://rubygems.org/downloads/blockenspiel-0.5.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
== Blockenspiel
Blockenspiel is a helper library designed to make it easy to implement DSL
blocks. It is designed to be comprehensive and robust, supporting most common
usage patterns, and working correctly in the presence of nested blocks and
multithreading.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n blockenspiel-0.5.0
gem spec %{SOURCE0} -l --ruby > rubygem-blockenspiel.gemspec

%build
gem build rubygem-blockenspiel.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
blockenspiel-0.5.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/blockenspiel-0.5.0
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/blockenspiel-0.5.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/Blockenspiel.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/History.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/ImplementingDSLblocks.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/Version
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel/builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel/dsl_setup.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel/impl.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel/unmixer_rubinius.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel/unmixer_unimplemented.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel/versionomy.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/lib/blockenspiel_unmixer_jruby.jar
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/files/file1.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/tc_basic.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/tc_behaviors.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/tc_dsl_attrs.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/tc_dsl_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/tc_dynamic.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/tc_embedded_block.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/tc_mixins.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/tc_modules.rb
/usr/lib64/ruby/gems/2.3.0/gems/blockenspiel-0.5.0/test/tc_version.rb
/usr/lib64/ruby/gems/2.3.0/specifications/blockenspiel-0.5.0.gemspec
