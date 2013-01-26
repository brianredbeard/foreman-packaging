%define rbname railties
%define version 3.0.19
%define release 1

Summary: Tools for creating, working with, and running Rails applications.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyonrails.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
Requires: rubygem-rake >= 0.8.7
Requires: rubygem-thor => 0.14.4
Requires: rubygem-thor < 0.15
Requires: rubygem-rdoc => 3.4
Requires: rubygem-rdoc < 4

Requires: rubygem-activesupport = %{version}
Requires: rubygem-actionpack = %{version}

BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(railties) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Rails internals: application bootup, plugins, generators, and rake tasks.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/railstie-%{version}/CHANGELOG
%{gemdir}/gems/railstie-%{version}/README.rdoc
%{gemdir}/gems/railstie-%{version}/guides/assets/images/belongs_to.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/book_icon.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/bullet.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/challenge.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/chapters_icon.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/check_bullet.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/credits_pic_blank.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/csrf.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/customized_error_messages.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/edge_badge.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/error_messages.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/feature_tile.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/footer_tile.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/fxn.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/grey_bullet.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/habtm.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/has_many.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/has_many_through.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/has_one.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/has_one_through.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/header_backdrop.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/header_tile.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/i18n/demo_localized_pirate.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/i18n/demo_translated_en.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/i18n/demo_translated_pirate.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/i18n/demo_translation_missing.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/i18n/demo_untranslated.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/1.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/10.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/11.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/12.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/13.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/14.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/15.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/2.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/3.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/4.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/5.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/6.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/7.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/8.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/callouts/9.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/caution.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/example.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/home.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/important.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/next.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/note.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/prev.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/README
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/tip.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/up.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/icons/warning.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/jaimeiniesta.jpg
%{gemdir}/gems/railstie-%{version}/guides/assets/images/nav_arrow.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/polymorphic.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/posts_index.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/rails_guides_logo.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/rails_logo_remix.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/rails_welcome.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/session_fixation.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/tab_grey.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/tab_info.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/tab_note.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/tab_red.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/tab_yellow.gif
%{gemdir}/gems/railstie-%{version}/guides/assets/images/tab_yellow.png
%{gemdir}/gems/railstie-%{version}/guides/assets/images/validation_error_messages.png
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/guides.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushAppleScript.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushAS3.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushBash.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushColdFusion.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushCpp.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushCSharp.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushCss.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushDelphi.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushDiff.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushErlang.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushGroovy.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushJava.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushJavaFX.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushJScript.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPerl.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPhp.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPlain.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPowerShell.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushPython.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushRuby.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushSass.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushScala.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushSql.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushVb.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shBrushXml.js
%{gemdir}/gems/railstie-%{version}/guides/assets/javascripts/syntaxhighlighter/shCore.js
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/main.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/print.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/reset.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/style.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCore.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreDefault.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreDjango.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreEclipse.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreEmacs.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreFadeToGrey.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreMDUltra.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreMidnight.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shCoreRDark.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeDefault.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeDjango.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeEclipse.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeEmacs.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeFadeToGrey.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeMDUltra.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeMidnight.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeRailsGuides.css
%{gemdir}/gems/railstie-%{version}/guides/assets/stylesheets/syntaxhighlighter/shThemeRDark.css
%{gemdir}/gems/railstie-%{version}/guides/rails_guides/generator.rb
%{gemdir}/gems/railstie-%{version}/guides/rails_guides/helpers.rb
%{gemdir}/gems/railstie-%{version}/guides/rails_guides/indexer.rb
%{gemdir}/gems/railstie-%{version}/guides/rails_guides/levenshtein.rb
%{gemdir}/gems/railstie-%{version}/guides/rails_guides/textile_extensions.rb
%{gemdir}/gems/railstie-%{version}/guides/rails_guides.rb
%{gemdir}/gems/railstie-%{version}/guides/source/2_2_release_notes.textile
%{gemdir}/gems/railstie-%{version}/guides/source/2_3_release_notes.textile
%{gemdir}/gems/railstie-%{version}/guides/source/3_0_release_notes.textile
%{gemdir}/gems/railstie-%{version}/guides/source/action_controller_overview.textile
%{gemdir}/gems/railstie-%{version}/guides/source/action_mailer_basics.textile
%{gemdir}/gems/railstie-%{version}/guides/source/action_view_overview.textile
%{gemdir}/gems/railstie-%{version}/guides/source/active_record_basics.textile
%{gemdir}/gems/railstie-%{version}/guides/source/active_record_querying.textile
%{gemdir}/gems/railstie-%{version}/guides/source/active_record_validations_callbacks.textile
%{gemdir}/gems/railstie-%{version}/guides/source/active_support_core_extensions.textile
%{gemdir}/gems/railstie-%{version}/guides/source/ajax_on_rails.textile
%{gemdir}/gems/railstie-%{version}/guides/source/api_documentation_guidelines.textile
%{gemdir}/gems/railstie-%{version}/guides/source/association_basics.textile
%{gemdir}/gems/railstie-%{version}/guides/source/caching_with_rails.textile
%{gemdir}/gems/railstie-%{version}/guides/source/command_line.textile
%{gemdir}/gems/railstie-%{version}/guides/source/configuring.textile
%{gemdir}/gems/railstie-%{version}/guides/source/contribute.textile
%{gemdir}/gems/railstie-%{version}/guides/source/contributing_to_ruby_on_rails.textile
%{gemdir}/gems/railstie-%{version}/guides/source/credits.html.erb
%{gemdir}/gems/railstie-%{version}/guides/source/debugging_rails_applications.textile
%{gemdir}/gems/railstie-%{version}/guides/source/form_helpers.textile
%{gemdir}/gems/railstie-%{version}/guides/source/generators.textile
%{gemdir}/gems/railstie-%{version}/guides/source/getting_started.textile
%{gemdir}/gems/railstie-%{version}/guides/source/i18n.textile
%{gemdir}/gems/railstie-%{version}/guides/source/index.html.erb
%{gemdir}/gems/railstie-%{version}/guides/source/initialization.textile
%{gemdir}/gems/railstie-%{version}/guides/source/layout.html.erb
%{gemdir}/gems/railstie-%{version}/guides/source/layouts_and_rendering.textile
%{gemdir}/gems/railstie-%{version}/guides/source/migrations.textile
%{gemdir}/gems/railstie-%{version}/guides/source/nested_model_forms.textile
%{gemdir}/gems/railstie-%{version}/guides/source/performance_testing.textile
%{gemdir}/gems/railstie-%{version}/guides/source/plugins.textile
%{gemdir}/gems/railstie-%{version}/guides/source/rails_application_templates.textile
%{gemdir}/gems/railstie-%{version}/guides/source/rails_on_rack.textile
%{gemdir}/gems/railstie-%{version}/guides/source/routing.textile
%{gemdir}/gems/railstie-%{version}/guides/source/ruby_on_rails_guides_guidelines.textile
%{gemdir}/gems/railstie-%{version}/guides/source/security.textile
%{gemdir}/gems/railstie-%{version}/guides/source/testing.textile
%{gemdir}/gems/railstie-%{version}/guides/w3c_validator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/all.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/application/bootstrap.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/application/configurable.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/application/configuration.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/application/finisher.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/application/railties.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/application.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/backtrace_cleaner.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/cli.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/code_statistics.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/application.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/benchmarker.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/console.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/dbconsole.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/destroy.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/generate.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/plugin.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/profiler.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/runner.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/server.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands/update.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/commands.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/configuration.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/console/app.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/console/helpers.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/console/sandbox.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/deprecation.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/engine/configurable.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/engine/configuration.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/engine.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/actions.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/active_model.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/base.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/controller/controller_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/controller/templates/view.html.erb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/mailer/mailer_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/mailer/templates/view.text.erb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/scaffold/scaffold_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/scaffold/templates/_form.html.erb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/scaffold/templates/edit.html.erb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/scaffold/templates/index.html.erb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/scaffold/templates/new.html.erb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb/scaffold/templates/show.html.erb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/erb.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/generated_attribute.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/migration.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/named_base.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/app_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/app/controllers/application_controller.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/app/helpers/application_helper.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/app/views/layouts/application.html.erb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/application.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/boot.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/frontbase.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/ibm_db.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/jdbc.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/jdbcmysql.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/jdbcpostgresql.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/jdbcsqlite3.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/mysql.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/oracle.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/postgresql.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/databases/sqlite3.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/environment.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/environments/development.rb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/environments/production.rb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/environments/test.rb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/initializers/backtrace_silencers.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/initializers/inflections.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/initializers/mime_types.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/initializers/secret_token.rb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/initializers/session_store.rb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/locales/en.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config/routes.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/config.ru
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/db/seeds.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/doc/README_FOR_APP
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/Gemfile
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/gitignore
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/404.html
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/422.html
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/500.html
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/favicon.ico
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/images/rails.png
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/index.html
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/javascripts/application.js
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/javascripts/controls.js
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/javascripts/dragdrop.js
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/javascripts/effects.js
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/javascripts/prototype.js
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/javascripts/rails.js
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/robots.txt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/Rakefile
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/README
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/script/rails
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/test/performance/browsing_test.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/test/test_helper.rb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/controller/controller_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/controller/templates/controller.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/controller/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/generator/generator_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/generator/templates/%file_name%_generator.rb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/generator/templates/USAGE.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/generator/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/helper/helper_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/helper/templates/helper.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/helper/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/integration_test/integration_test_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/integration_test/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/migration/migration_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/migration/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/model/model_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/model/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/observer/observer_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/observer/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/performance_test/performance_test_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/performance_test/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/plugin_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/templates/init.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/templates/install.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/templates/lib/%file_name%.rb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/templates/lib/tasks/%file_name%_tasks.rake.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/templates/MIT-LICENSE.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/templates/Rakefile.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/templates/README.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/templates/uninstall.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/plugin/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/resource/resource_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/resource/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/scaffold/scaffold_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/scaffold/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/scaffold_controller/scaffold_controller_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/scaffold_controller/templates/controller.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/scaffold_controller/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/session_migration/session_migration_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/session_migration/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/stylesheets/stylesheets_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/stylesheets/templates/scaffold.css
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/stylesheets/USAGE
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/resource_helpers.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_case.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/controller/controller_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/controller/templates/functional_test.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/helper/helper_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/helper/templates/helper_test.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/integration/integration_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/integration/templates/integration_test.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/mailer/mailer_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/mailer/templates/functional_test.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/model/model_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/model/templates/fixtures.yml
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/model/templates/unit_test.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/observer/observer_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/observer/templates/unit_test.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/performance/performance_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/performance/templates/performance_test.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/plugin/plugin_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/plugin/templates/%file_name%_test.rb.tt
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/plugin/templates/test_helper.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/scaffold/scaffold_generator.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit/scaffold/templates/functional_test.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/test_unit.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/info.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/info_controller.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/info_routes.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/initializable.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/paths.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/performance_test_help.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/plugin.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/rack/debugger.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/rack/log_tailer.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/rack/logger.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/rack/static.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/rack.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/railtie/configurable.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/railtie/configuration.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/railtie.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/ruby_version_check.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/rubyprof_ext.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/script_rails_loader.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/source_annotation_extractor.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks/annotations.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks/documentation.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks/framework.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks/log.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks/middleware.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks/misc.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks/routes.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks/statistics.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks/tmp.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/tasks.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/test_help.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/test_unit/railtie.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/test_unit/testing.rake
%{gemdir}/gems/railstie-%{version}/lib/rails/version.rb
%{gemdir}/gems/railstie-%{version}/lib/rails.rb
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/app/mailers/.empty_directory
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/app/models/.empty_directory
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/public/stylesheets/.empty_directory
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/test/fixtures/.empty_directory
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/test/functional/.empty_directory
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/test/integration/.empty_directory
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/app/templates/test/unit/.empty_directory
%{gemdir}/gems/railstie-%{version}/lib/rails/generators/rails/generator/templates/templates/.empty_directory

%doc %{gemdir}/doc/railstie-%{version}
%{gemdir}/cache/railstie-%{version}.gem
%{gemdir}/specifications/railstie-%{version}.gemspec

%changelog
* Fri Jan 25 2013 shk@redhat.com 3.0.19-1
- Updated to 3.0.19
