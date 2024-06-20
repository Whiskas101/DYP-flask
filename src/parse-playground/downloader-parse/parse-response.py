from bs4 import BeautifulSoup

#response1: Type of page where the content is rendered directly on the requested page
response1 = """
<!DOCTYPE html>
<html  dir="ltr" lang="en" xml:lang="en" class="no-js">
<head>
    <title>CAC404-22-A-AIML: week 1 ppython_uw</title>
    <link rel="shortcut icon" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/favicon"/>
    <link rel="stylesheet" href="//mydy.dypatil.edu/rait/pluginfile.php/1/theme_essential/style/1709815567/essential.css">          
  
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, CAC404-22-A-AIML: week 1 ppython_uw" />
<script type="text/javascript">
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/mydy.dypatil.edu\/rait","sesskey":"z9VmVG5VJO","loadingicon":"https:\/\/mydy.dypatil.edu\/rait\/theme\/image.php\/essential\/core\/1709815567\/i\/loading_small","themerev":"1709815567","slasharguments":1,"theme":"essential","jsrev":"1709815567","admin":"admin","svgicons":true};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''};if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else me.path=component+'/'+component+'.'+me.type};
YUI_config = {"debug":false,"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?m\/1709815567\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"m\/1709815567\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-checknet":{"requires":["base-base","moodle-core-notification-alert","io-base"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-dock":{"requires":["base","node","event-custom","event-mouseenter","event-resize","escape","moodle-core-dock-loader"]},"moodle-core-dock-loader":{"requires":["escape"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-formautosubmit":{"requires":["base","event-key"]},"moodle-core-formchangechecker":{"requires":["base","event-focus"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core_availability-form":{"requires":["base","node","event","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-calendar-info":{"requires":["base","node","event-mouseenter","event-key","overlay","moodle-calendar-info-skin"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-modchooser":{"requires":["moodle-core-chooserdialogue","moodle-course-coursebase"]},"moodle-course-toolboxes":{"requires":["node","base","event-key","node","io","moodle-course-coursebase","moodle-course-util"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-passwordunmask":{"requires":["node","base"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-showadvanced":{"requires":["node","base","selector-css3"]},"moodle-core_message-messenger":{"requires":["escape","handlebars","io-base","moodle-core-notification-ajaxexception","moodle-core-notification-alert","moodle-core-notification-dialogue","moodle-core-notification-exception"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-qbankmanager":{"requires":["node","selector-css3"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_cohort-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_customcert-rearrange":{"requires":["dd-delegate","dd-drag"]},"moodle-mod_forum-subscriptiontoggle":{"requires":["base-base","io-base"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-quizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-core-notification-dialogue"]},"moodle-mod_quiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_navigation-navigation":{"requires":["base","io-base","node","event-synthetic","event-delegate","json-parse"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-format_grid-gridkeys":{"requires":["event-nav-keys"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_html-button":{"requires":["moodle-editor_atto-plugin","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1709815567\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.mathjax.org\/mathjax\/2.5-latest\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
</script>
<link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" /><script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js&amp;rollup/1709815567/mcore-min.js"></script><script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/jquery-1.11.2.min.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/ui-1.11.4/jquery-ui.min.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/bootstrap_2_3_2_min.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/jBreadCrumb_1_1.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/fitvids_1_1_1.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/anti_gravity_1_1.js"></script>
<script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/theme/styles.php/essential/1709815567/all" />
<link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/jquery-ui.css" />
<link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/style.css" />
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/javascript-static.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/head"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google web fonts -->
    <!--<link href='http://fonts.googleapis.com/css?family=Domine' rel='stylesheet' type='text/css'>-->
    <!-- iOS Homescreen Icons -->
    
<link rel="apple-touch-icon-precomposed" sizes="57x57" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone"/>
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad"/>
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone_retina"/>
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad_retina"/>    <!-- Start Analytics -->
        <!-- End Analytics -->

    <!--include custom fonts-->
    <style>
        @font-face {
            font-family: "Minion Pro Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/Minion-Pro-Regular.ttf');
        }
        @font-face {
            font-family: "SourceSansPro-Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Regular.ttf');
        }
        @font-face {
            font-family: "SourceSansPro-Light";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Light.ttf');
        }
        @font-face {
            font-family: "SourceSansPro-Semibold";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Semibold.ttf');
        }
    </style>

    <script type="text/javascript">
		$(document).ready(function() {
	  	//var $pwidth = $(window).width();
			//var $loggedin = $('body').hasClass('loggedin');

			/*if($pwidth >= 768){
				$('.offcanvas, #content-container').addClass('active');
			}*/

		  $('[data-toggle=offcanvas]').click(function() {

		  var $pwidth = $(window).width();
			$('.offcanvas').toggleClass('active');
			$('#content-container').toggleClass('active');

			//do this when in nmobile view
			var $main = $('main').hasClass('active');
			if($pwidth <= 480 ){

				if( $main == true){
					$('body, html').addClass('noscroll');
				}else{
					$('body, html').removeClass('noscroll');
				}
			}

			//do this when in tab/desktop view
			if($pwidth >= 481 ){

				//var $main = $('main').hasClass('active');

				if( $main == false){
					$('body, html').removeClass('noscroll');
				}
			}

		  });
        });
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS starts here -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-62316529-3"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag("js", new Date());
            gtag("config", "UA-62316529-3");
        </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS ends here -->
</head>
<body  id="page-mod-presentation-view" class="format-topcoll  path-mod path-mod-presentation dir-ltr lang-en yui-skin-sam yui3-skin-sam mydy-dypatil-edu--rait pagelayout-incourse course-5922 context-732280 cmid-611990 category-879 desktopdevice pagewidthnormal categoryicons zoomin two-column  has-region-side-pre used-region-side-pre has-region-footer-left empty-region-footer-left has-region-footer-middle empty-region-footer-middle has-region-footer-right empty-region-footer-right side-pre-only">

<div class="skiplinks"><a class="skip" href="#maincontent">Skip to main content</a></div>
<script type="text/javascript">
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>


<header role="banner">
    <div id="page-header" class="clearfix oldnavbar">
        <div class="container-fluid">
            <div class="row-fluid">
                <!-- HEADER: LOGO AREA -->
                <div class="ecol12 pull-left">
                                            <a class="logo" href="//mydy.dypatil.edu/rait" title="Home"></a>
                    					<nav role="navigation">
						<div class="topnavbar navbar oldnavbar moodle-has-zindex">
							<div class="container-fluid navbar-inner">
								<div class="row-fluid">
									<div class="pull-right">
										<div class="usermenu">
											<ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=z9VmVG5VJO"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>										</div>
										<div class="messagemenu">
											<ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>										</div>
										<div class="messagemenu messagemenu_video">
											<ul class="nav"><li><a class="videotutorial" href="https://mydy.dypatil.edu/rait/mod/page/view.php?id=101">Training Video</a></li></ul>										</div>
										<!--<div class="messagemenu">-->
																					<!--</div>-->
										<!--<div class="messagemenu">-->
																					<!--</div>-->
										<div class="gotobottommenu">
											<ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>										</div>
									</div>
								</div>
							</div>
						</div>
					</nav>
                </div>


            </div>
        </div>
    </div>
    <nav role="navigation">
        <div id='essentialnavbar' class="navbar oldnavbar moodle-has-zindex">
            <div class="container-fluid navbar-inner">
                <div class="row-fluid">
                    <div class="custommenus pull-left">
                        <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </a>
                                            <!--<div class="pull-right">-->
                    <!--    <div class="usermenu">-->
                    <!--        <ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=z9VmVG5VJO"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>-->
                    <!--    </div>-->
                    <!--    <div class="messagemenu">-->
                    <!--        <ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>-->
                    <!--    </div>-->
                    <!--    <div class="messagemenu">-->
                    <!--        <ul class="nav"></ul>-->
                    <!--    </div>-->
                    <!--    <div class="messagemenu">-->
                    <!--        <ul class="nav"></ul>-->
                    <!--    </div>-->
                    <!--    <div class="gotobottommenu">-->
                    <!--        <ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>-->
                    <!--    </div>-->
                    <!--</div>-->
                        <div class="nav-collapse collapse pull-left">
                            <div id="custom_menu_language">
                                <ul class="nav"></ul>                            </div>
                            <div id="custom_menu_courses">
                                <ul class="nav"></ul>                            </div>
                                                        <div id="custom_menu">
                                <ul class="nav"></ul>                            </div>
                            <div id="custom_menu_activitystream">
                                                            </div>
                            <ul class="nav pull-left">
                                                                <li class="hbl"><a href="#" class="moodlezoom"><i class="fa fa-outdent fa-lg"></i> <span class="zoomdesc"></span></a></li>
                                <li class="sbl"><a href="#" class="moodlezoom"><i class="fa fa-indent fa-lg"></i> <span class="zoomdesc"></span></a></li>
                                                             </ul>

                    <!--******************code added by anil-started here*******************-->
							<div id="custom_menu_topmenu">
                                 <!--*********code added by anil*************-->
                                <ul class="nav"><li><a href="https://mydy.dypatil.edu/rait/" class="navbarlinks">Home</a></li><li><a href="http://m.p-y.tm/PUPRTT" class="navbarlinks" target="_blank">Fee Payment</a></li><li><a href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php" class="navbarlinks">Exams</a></li><li><a href="https://mydy.dypatil.edu/rait/local/dypmarket/index.php" id="marketplace">Market Place</a></li></ul>                    <!--******************code added by anil-ended here*******************-->
							</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</header>

<div id="page" class="container-fluid">
    <div id="page-navbar" class="clearfix row-fluid">
        <div
            class="breadcrumb-nav pull-left"><ul class="breadcrumb style2"><li style="z-index:99;"><a href="https://mydy.dypatil.edu/rait/my/">Dashboard</a></li><li style="z-index:98;"><a title="Programming with Python" href="https://mydy.dypatil.edu/rait/course/view.php?id=5922">CAC404-22-A-AIML</a></li><li style="z-index:97;"><span tabindex="0">Week 1</span></li><li style="z-index:96;"><a title="Presentation (Download)" href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=611990">week 1 ppython_uw</a></li></ul></div>
        <nav
            class="breadcrumb-button pull-right"></nav>
    </div>
    <section role="main-content">
        <!-- Start Main Regions -->
        <div id="page-content" class="row-fluid">
            <div id="region-bs-main-and-pre" class="span12">
                <div class="row-fluid">
                                            <section id="region-main" class="span9 pull-right">
                    <h1 class="coursetitle">Programming with Python</h1><div class="bor"></div>                                                        <div role="main"><span id="maincontent"></span><h2>week 1 ppython_uw</h2><div class="presentationcontent presentationpdf">
  <object id="presentationobject" data="https://mydy.dypatil.edu/rait/pluginfile.php/732280/mod_presentation/content/1/week%201%20ppython_uw.pdf" type="application/pdf" width="800" height="600">
    <param name="src" value="https://mydy.dypatil.edu/rait/pluginfile.php/732280/mod_presentation/content/1/week%201%20ppython_uw.pdf" />
    Click <a href="https://mydy.dypatil.edu/rait/pluginfile.php/732280/mod_presentation/content/1/week%201%20ppython_uw.pdf" >week 1 ppython_uw.pdf</a> link to view the file.
  </object>
</div><div id="fb-root"></div><div id="myratings"></div><div id="presentation_pages"><div class="like_unlike"><div id="contents_29411" style="float: left;"><div id="label_like_29411" style="float: left; padding: 0 8px 0 0;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;presentation&quot;, 611990, 29411, 5922, 0)" /></div><span  id="count_likearea" class="count_likearea_29411"><a id="anchorclass_29411" href="javascript:void(0)" onClick="fnViewAllLikes(29411)">0</a></span><div class="courselike" id="like_list_29411" style="display: none;"><div style="float: right; cursor: pointer;" class="closeicon29411"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="like_closeicon" /></div><span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Likes</b></span><div class="like_29411"></div></div><div id="label_unlike_29411" style="float: left; padding: 0 8px 0 10px; margin-top:5px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Dislike" id="unlikeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;presentation&quot;, 611990, 29411, 5922, 1)" /></div><span id="count_unlikearea"  class="count_unlikearea_29411"><a id="anchorclass_29411" href="javascript:void(0)" onClick="fnViewAllunLikes(29411)">0</a></span><div class="courseunlike" id="unlike_list_29411" style="display: none;"><div style="float: right; cursor: pointer;" class="closeicon29411"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="unlike_closeicon" /></div><span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Unlikes</b></span><div class="unlike_29411"></div></div></div></div><div class="radiostars"><div class="overall_ratings_29411" style="float: left; cursor: pointer;"><img title='0 out of 5' src='https://mydy.dypatil.edu/rait/local/ratings/pix/star0.png'  onclick='fnViewAllRatings(5922, 611990, 29411, "presentation", "https://mydy.dypatil.edu/rait", "week 1 ppython_uw")'/></div><div class="overall_users">(<font class='totalcount_29411'>0</font> users)</div></div><div class="mycomment"><a id="anchorclass_29411" href="javascript:void(0)" onClick="fnViewAllComments(29411)"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/comment.png" title="Comment" id="custom_icons" /></a>&nbsp;(<font class="commentcount_29411">0</font>)<div class="coursecomment" id="comment_list_29411" style="display: none;"><div style="float: right; cursor: pointer;" class="closeicon29411"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="comment_closeicon" /></div><textarea name="commentarea" id="mycomment_29411" rows="2" cols="50"></textarea><a class="commentclick_29411" href="javascript:void(0)" onClick="fnComment(5922, 611990, 29411, &quot;presentation&quot;, &quot;https://mydy.dypatil.edu/rait&quot;)" style="font-size: 12px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/add-comment.gif" /></a><div class="comment_29411"></div></div></div></div></div>                                                    </section>
                    <aside id="block-region-side-pre" class="span3 desktop-first-column block-region" data-blockregion="side-pre" data-droptarget="1"><a href="#sb-1" class="skip-block">Skip My tasks</a><div id="inst19" class="block_universitystructure  block" role="complementary" data-block="universitystructure" data-instanceid="19" aria-labelledby="instance-19-header" data-dockable="1"><div class="header"><div class="title"><div class="block_action"></div><h2 id="instance-19-header">My tasks</h2></div></div><div class="content"><ul class="block_tree list"><li class="type_unknown depth_1 contains_branch simple_invisible"><p class="tree_item branch active_tree_node navigation_node" ><span  ><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span><li class="type_course depth_2 contains_branch"><p class="tree_item branch hasicon active_tree_node" ><span class="usdimmed_text" >My Learnings</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/timetable/calendarview.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">TimeTable Calendar</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/myacademics/transcript.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Transcript</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/academiccalendar"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Academic Calendar</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/feemanagement/studentfeedetails.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Fee Details</a></p></li></ul><li class="type_category depth_3 contains_branch"><p class="tree_item branch active_tree_node" ><span class="usdimmed_text" >Examination</span><ul><li class="type_course depth_4 collapsed contains_branch"><p class="tree_item nomodule hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php">Scheduled Exams</a></p></li><li class="type_course depth_4 collapsed contains_branch"><p class="tree_item nomodule hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/examination/studentresults.php">Student Examsresults </a></p></li></ul></li><li class="type_course depth_3 contains_branch"><p class="tree_item branch hasicon active_tree_node" ><span class="usdimmed_text" >My Profile</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/users/profile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">View Profile</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Edit Profile</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/users/change_password.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Change Password</a></p></li></ul></li></ul></li></ul></div></div><span id="sb-1" class="skip-block-to"></span><a href="#sb-3" class="skip-block">Skip Administration</a><div id="inst5" class="block_settings  block" role="navigation" data-block="settings" data-instanceid="5" aria-labelledby="instance-5-header" data-dockable="1"><div class="header"><div class="title"><div class="block_action"></div><h2 id="instance-5-header">Administration</h2></div></div><div class="content"><div id="settingsnav" class="box block_tree_box"><ul class="block_tree list"><li class="type_course collapsed contains_branch" aria-expanded="false"><p class="tree_item branch root_node"><span tabindex="0">Course administration</span></p><ul><li class="type_setting collapsed item_with_icon"><p class="tree_item leaf"><a href="https://mydy.dypatil.edu/rait/grade/report/index.php?id=5922"><i class="fa fa-table icon" title=""><img alt="" class="smallicon navicon" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/grades" /></i>Grades</a></p></li></ul></li></ul></div></div></div><span id="sb-3" class="skip-block-to"></span><a href="#sb-5" class="skip-block">Skip Previous semester classes</a><div id="inst31230" class="block_stu_previousclasses  block" role="complementary" data-block="stu_previousclasses" data-instanceid="31230" aria-labelledby="instance-31230-header" data-dockable="1"><div class="header"><div class="title"><div class="block_action"></div><h2 id="instance-31230-header">Previous semester classes</h2></div></div><div class="content"><ul class="block_tree list"><li class="type_unknown depth_1 contains_branch simple_invisible"><p class="tree_item branch active_tree_node navigation_node" ><span  ><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span><li class="type_course depth_2 contains_branch"><p class="tree_item branch hasiconactive_tree_node" ><span class="usdimmed_text" >Semester I</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4642" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics I</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4643" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Structered Programming</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4644" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Electronics Engineering</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4645" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Physics</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4646" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">English For Engineers</a></p></li></ul></li><li class="type_course depth_2 collapsed contains_branch"><p class="tree_item branch hasicon" ><span class="usdimmed_text" >Semester II</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5067" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics-II</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5068" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Chemistry II</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5069" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Data Structures</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5071" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Digital Logic Design</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5072" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Environmental Studies</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5070" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Communication Engineering</a></p></li></ul></li><li class="type_course depth_2 collapsed contains_branch"><p class="tree_item branch hasicon" ><span class="usdimmed_text" >Semester III</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5197" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Database Management System</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5198" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Design and Analysis of Algorithms</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5199" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Object Oriented Programming</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5200" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Computer Organization & Architecture</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5201" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Statistical Methods</a></p></li></ul></li><li class="type_course depth_2 collapsed contains_branch"><p class="tree_item branch hasicon" ><span class="usdimmed_text" >Semester IV</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5919" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Artificial Intelligence</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5920" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Software Engineering</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5921" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Operating System</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5922" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Programming with Python</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5923" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Formal Language Automata Language</a></p></li></ul></li></ul></li></ul></div></div><span id="sb-5" class="skip-block-to"></span></aside>                </div>
                            </div>
        </div>
        <!-- End Main Regions -->
    </section>
</div>

    <footer role="contentinfo" id="page-footer">
        <div class="container-fluid">
                        <div class="row-fluid footerblocks">
                <div class="span8 pull-left footersite-text">
                    <p><h4>'Education is not the learning of many facts </h4></p><p><h4>but the training of the mind to think.' - Albert Einstein</h4></p>
                </div>
                <div class="span4 pull-right footersite-icons">
                                    </div>
            </div>
            <div class="row-fluid footerblocks">
                <div class="span4 pull-left">
                    <div class="column">
                        <aside id="block-region-footer-left" class="block-region" data-blockregion="footer-left" data-droptarget="1"></aside>                    </div>
                </div>
                <div class="span4 center">
                    <div class="column">
                        <aside id="block-region-footer-middle" class="block-region" data-blockregion="footer-middle" data-droptarget="1"></aside>                    </div>
                </div>
                <div class="span4 pull-right">
                    <div class="column">
                        <aside id="block-region-footer-right" class="block-region" data-blockregion="footer-right" data-droptarget="1"></aside>                    </div>
                </div>
            </div>
            <div class="footerlinks row-fluid">
                <hr/>
                <span class="helplink"></span>
                                            </div>
            <div class="footerperformance row-fluid">
                            </div>
            <div class="footercredit row-fluid">
                The Essential theme is developed, enhanced and maintained by <a href="//about.me/gjbarnard" target="_blank">Gareth J Barnard</a>
            </div>
        </div>
    </footer>
    <a href="#top" class="back-to-top" ><i class="fa fa-angle-up "></i></a>
<!--js file commented and included in blocks/events instead of adding in theme footer-->
<!--<script src="https://cdn.rawgit.com/vast-engineering/jquery-popup-overlay/1.7.10/jquery.popupoverlay.js"></script>-->
<script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/custom_zoom.js"></script>
<script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/select2.min.js"></script>
<link href="https://mydy.dypatil.edu/rait/theme/essential/style/select2.min.css" rel="stylesheet" />

    <script type="text/javascript">
        jQuery(document).ready(function () {
            $('#id_cobaltcourseid').select2();
            $('#id_onlinecourseid').select2();
            jQuery('#essentialnavbar').affix({offset: {top: $('#page-header').height()}});$('#page').fitVids();        });
    </script>
<script type="text/javascript">
//<![CDATA[
var require = {
    baseUrl : 'https://mydy.dypatil.edu/rait/lib/requirejs.php/1709815567/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,

    paths: {
        jquery: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/jquery-1.11.2.min',
        jqueryui: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/ui-1.11.4/jquery-ui.min',
        jqueryprivate: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
</script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/require.min.js"></script>
<script type="text/javascript">
//<![CDATA[
require(['core/first'], function() {
;
require(["core/log"], function(amd) { amd.setConfig({"level":"warn"}); });
});
//]]>
</script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/ratings.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/facebook.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/twitter.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/footer"></script>
<script type="text/javascript">
//<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","viewallcourses":"View all courses","morehelp":"More help","loadinghelp":"Loading...","cancel":"Cancel","yes":"Yes","confirm":"Confirm","no":"No","areyousure":"Are you sure?","closebuttontitle":"Close","unknownerror":"Unknown error"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source","select":"Select"},"block":{"addtodock":"Move this to the dock","undockitem":"Undock this item","dockblock":"Dock {$a} block","undockblock":"Undock {$a} block","undockall":"Undock all","hidedockpanel":"Hide the dock panel","hidepanel":"Hide panel"},"langconfig":{"thisdirectionvertical":"btt"},"admin":{"confirmation":"Confirmation"}};
//]]>
</script>
<script type="text/javascript">
//<![CDATA[
var navtreeexpansions4 = [{"id":"expandable_branch_30_168056","key":"168056","type":30},{"id":"expandable_branch_30_168108","key":"168108","type":30},{"id":"expandable_branch_30_168109","key":"168109","type":30},{"id":"expandable_branch_30_168110","key":"168110","type":30},{"id":"expandable_branch_30_168111","key":"168111","type":30},{"id":"expandable_branch_30_168112","key":"168112","type":30},{"id":"expandable_branch_30_168113","key":"168113","type":30},{"id":"expandable_branch_30_168114","key":"168114","type":30},{"id":"expandable_branch_30_168115","key":"168115","type":30},{"id":"expandable_branch_30_168116","key":"168116","type":30},{"id":"expandable_branch_0_mycourses","key":"mycourses","type":0}];
//]]>
</script>
<script type="text/javascript">
//<![CDATA[
YUI().use('node', function(Y) {
M.util.load_flowplayer();
setTimeout("fix_column_widths()", 20);
Y.use("moodle-core-dock-loader",function() {M.core.dock.loader.initLoader();
});
 M.util.js_pending('random663b9ca9650b41'); Y.on('domready', function() { M.util.init_maximised_embed(Y, "presentationobject");  M.util.js_complete('random663b9ca9650b41'); });
Y.use("moodle-theme_essential-zoom",function() {M.theme_essential.zoom.init();
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"19","instance":"19","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"4","instance":"4","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"5","instance":"5","candock":true});
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"31230","instance":"31230","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"en"});
});
M.util.help_popups.setup(Y);
Y.use("moodle-core-popuphelp",function() {M.core.init_popuphelp();
});
M.util.init_block_hider(Y, {"id":"inst19","title":"My tasks","preference":"block19hidden","tooltipVisible":"Hide My tasks block","tooltipHidden":"Show My tasks block"});
M.util.init_block_hider(Y, {"id":"inst5","title":"Administration","preference":"block5hidden","tooltipVisible":"Hide Administration block","tooltipHidden":"Show Administration block"});
M.util.init_block_hider(Y, {"id":"inst31230","title":"Previous semester classes","preference":"block31230hidden","tooltipVisible":"Hide Previous semester classes block","tooltipHidden":"Show Previous semester classes block"});
 M.util.js_pending('random663b9ca9650b46'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random663b9ca9650b46'); });

});
//]]>
</script>
</body>
</html>
"""

#response2: Type of page where the content is rendered within a flexpaper custom pdf viewer (the worst one)
response2 = """
<div id="documentViewer" class="flexpaper_viewer" style="position:relative;width:100%;height:100%;"></div><script type="text/javascript" src="https://mydy.dypatil.edu/rait/mod/flexpaper/js/jquery.min.js"></script>
		<script type="text/javascript" src="https://mydy.dypatil.edu/rait/mod/flexpaper/js/jquery.extensions.min.js"></script>
        <!--[if gte IE 10 | !IE ]><!-->
        <script type="text/javascript" src="https://mydy.dypatil.edu/rait/mod/flexpaper/js/three.min.js"></script>
        <!--<![endif]-->
		<script type="text/javascript" src="https://mydy.dypatil.edu/rait/mod/flexpaper/js/flexpaper.js"></script>
		<script type="text/javascript" src="https://mydy.dypatil.edu/rait/mod/flexpaper/js/flexpaper_handlers.js"></script>
		<link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/mod/flexpaper/css/flexpaper.css" />


	        <script type="text/javascript">
		       
	        $('#documentViewer').FlexPaperViewer(
				 { config : {

						 IMGFiles : 'pdf/12.png',
						 PDFFile : 'https://mydy.dypatil.edu/rait/pluginfile.php/733425/mod_flexpaper/content/1/week%206%20ppython_uw_%20projects.pdf',
						 Scale : 0.6,
						 ZoomTransition : 'easeOut',
						 ZoomTime : 0.5,
						 ZoomInterval : 0.1,
						 FitPageOnLoad : true,
						 FitWidthOnLoad : false,
						 FullScreenAsMaxWindow : false,
						 ProgressiveLoading : false,
						 MinZoomSize : 0.2,
						 MaxZoomSize : 5,
						 SearchMatchAll : false,
						 InitViewMode : '',
						 MixedMode : false,
						 EnableWebGL : true,
						 ViewModeToolsVisible : true,
						 ZoomToolsVisible : true,
						 NavToolsVisible : true,
						 CursorToolsVisible : true,
						 SearchToolsVisible : true,
						 JSONDataType : 'jsonp',
						 key : '$ec2255d5ea91ec492ce',
                                                 WMode : 'transparent',
  						 localeChain: 'en_US'
						 }}
			    );
	        </script>
			<div id="fb-root"></div><div id="myratings"></div><div id="flexpaper_pages"><div class="like_unlike"><div id="contents_141136" style="float: left;"><div id="label_like_141136" style="float: left; padding: 0 8px 0 0;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;flexpaper&quot;, 613117, 141136, 5922, 0)" /></div><span  id="count_likearea" class="count_likearea_141136"><a id="anchorclass_141136" href="javascript:void(0)" onClick="fnViewAllLikes(141136)">0</a></span><div class="courselike" id="like_list_141136" style="display: none;"><div style="float: right; cursor: pointer;" class="closeicon141136"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="like_closeicon" /></div><span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Likes</b></span><div class="like_141136"></div></div><div id="label_unlike_141136" style="float: left; padding: 0 8px 0 10px; margin-top:5px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Dislike" id="unlikeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;flexpaper&quot;, 613117, 141136, 5922, 1)" /></div><span id="count_unlikearea"  class="count_unlikearea_141136"><a id="anchorclass_141136" href="javascript:void(0)" onClick="fnViewAllunLikes(141136)">0</a></span><div class="courseunlike" id="unlike_list_141136" style="display: none;"><div style="float: right; cursor: pointer;" class="closeicon141136"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="unlike_closeicon" /></div><span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Unlikes</b></span><div class="unlike_141136"></div></div></div></div><div class="radiostars"><div class="overall_ratings_141136" style="float: left; cursor: pointer;"><img title='0 out of 5' src='https://mydy.dypatil.edu/rait/local/ratings/pix/star0.png'  onclick='fnViewAllRatings(5922, 613117, 141136, "flexpaper", "https://mydy.dypatil.edu/rait", "week 6 ppython_uw_ projects")'/></div><div class="overall_users">(<font class='totalcount_141136'>0</font> users)</div></div><div class="mycomment"><a id="anchorclass_141136" href="javascript:void(0)" onClick="fnViewAllComments(141136)"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/comment.png" title="Comment" id="custom_icons" /></a>&nbsp;(<font class="commentcount_141136">0</font>)<div class="coursecomment" id="comment_list_141136" style="display: none;"><div style="float: right; cursor: pointer;" class="closeicon141136"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="comment_closeicon" /></div><textarea name="commentarea" id="mycomment_141136" rows="2" cols="50"></textarea><a class="commentclick_141136" href="javascript:void(0)" onClick="fnComment(5922, 613117, 141136, &quot;flexpaper&quot;, &quot;https://mydy.dypatil.edu/rait&quot;)" style="font-size: 12px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/add-comment.gif" /></a><div class="comment_141136"></div></div></div></div>
"""


#response3: Type of page where the link to the resource is explicity made visible to the student
# altered response1 handling in such a way that both 1 and 3 can be handled together.
response3 = """
<!DOCTYPE html>
<html  dir="ltr" lang="en" xml:lang="en" class="no-js">
<head>
    <title>CAC403-22-A-AIML: ebook os</title>
    <link rel="shortcut icon" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/favicon"/>
    <link rel="stylesheet" href="//mydy.dypatil.edu/rait/pluginfile.php/1/theme_essential/style/1709815567/essential.css">          
  
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="moodle, CAC403-22-A-AIML: ebook os" />
<script type="text/javascript">
//<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/mydy.dypatil.edu\/rait","sesskey":"z9VmVG5VJO","loadingicon":"https:\/\/mydy.dypatil.edu\/rait\/theme\/image.php\/essential\/core\/1709815567\/i\/loading_small","themerev":"1709815567","slasharguments":1,"theme":"essential","jsrev":"1709815567","admin":"admin","svgicons":true};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''};if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else me.path=component+'/'+component+'.'+me.type};
YUI_config = {"debug":false,"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?m\/1709815567\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"m\/1709815567\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-checknet":{"requires":["base-base","moodle-core-notification-alert","io-base"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-dock":{"requires":["base","node","event-custom","event-mouseenter","event-resize","escape","moodle-core-dock-loader"]},"moodle-core-dock-loader":{"requires":["escape"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-formautosubmit":{"requires":["base","event-key"]},"moodle-core-formchangechecker":{"requires":["base","event-focus"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core_availability-form":{"requires":["base","node","event","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-calendar-info":{"requires":["base","node","event-mouseenter","event-key","overlay","moodle-calendar-info-skin"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-modchooser":{"requires":["moodle-core-chooserdialogue","moodle-course-coursebase"]},"moodle-course-toolboxes":{"requires":["node","base","event-key","node","io","moodle-course-coursebase","moodle-course-util"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-passwordunmask":{"requires":["node","base"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-showadvanced":{"requires":["node","base","selector-css3"]},"moodle-core_message-messenger":{"requires":["escape","handlebars","io-base","moodle-core-notification-ajaxexception","moodle-core-notification-alert","moodle-core-notification-dialogue","moodle-core-notification-exception"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-qbankmanager":{"requires":["node","selector-css3"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_cohort-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_customcert-rearrange":{"requires":["dd-delegate","dd-drag"]},"moodle-mod_forum-subscriptiontoggle":{"requires":["base-base","io-base"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-quizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-core-notification-dialogue"]},"moodle-mod_quiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_navigation-navigation":{"requires":["base","io-base","node","event-synthetic","event-delegate","json-parse"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-format_grid-gridkeys":{"requires":["event-nav-keys"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_html-button":{"requires":["moodle-editor_atto-plugin","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1709815567\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.mathjax.org\/mathjax\/2.5-latest\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
</script>
<link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" /><script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js&amp;rollup/1709815567/mcore-min.js"></script><script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/jquery-1.11.2.min.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/ui-1.11.4/jquery-ui.min.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/bootstrap_2_3_2_min.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/jBreadCrumb_1_1.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/fitvids_1_1_1.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/anti_gravity_1_1.js"></script>
<script id="firstthemesheet" type="text/css">/** Required in order to fix style inclusion problems in IE with YUI **/</script><link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/theme/styles.php/essential/1709815567/all" />
<link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/jquery-ui.css" />
<link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/style.css" />
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/javascript-static.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/head"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google web fonts -->
    <!--<link href='http://fonts.googleapis.com/css?family=Domine' rel='stylesheet' type='text/css'>-->
    <!-- iOS Homescreen Icons -->
    
<link rel="apple-touch-icon-precomposed" sizes="57x57" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone"/>
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad"/>
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone_retina"/>
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad_retina"/>    <!-- Start Analytics -->
        <!-- End Analytics -->

    <!--include custom fonts-->
    <style>
        @font-face {
            font-family: "Minion Pro Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/Minion-Pro-Regular.ttf');
        }
        @font-face {
            font-family: "SourceSansPro-Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Regular.ttf');
        }
        @font-face {
            font-family: "SourceSansPro-Light";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Light.ttf');
        }
        @font-face {
            font-family: "SourceSansPro-Semibold";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Semibold.ttf');
        }
    </style>

    <script type="text/javascript">
		$(document).ready(function() {
	  	//var $pwidth = $(window).width();
			//var $loggedin = $('body').hasClass('loggedin');

			/*if($pwidth >= 768){
				$('.offcanvas, #content-container').addClass('active');
			}*/

		  $('[data-toggle=offcanvas]').click(function() {

		  var $pwidth = $(window).width();
			$('.offcanvas').toggleClass('active');
			$('#content-container').toggleClass('active');

			//do this when in nmobile view
			var $main = $('main').hasClass('active');
			if($pwidth <= 480 ){

				if( $main == true){
					$('body, html').addClass('noscroll');
				}else{
					$('body, html').removeClass('noscroll');
				}
			}

			//do this when in tab/desktop view
			if($pwidth >= 481 ){

				//var $main = $('main').hasClass('active');

				if( $main == false){
					$('body, html').removeClass('noscroll');
				}
			}

		  });
        });
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS starts here -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-62316529-3"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag("js", new Date());
            gtag("config", "UA-62316529-3");
        </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS ends here -->
</head>
<body  id="page-mod-resource-view" class="format-topcoll  path-mod path-mod-resource dir-ltr lang-en yui-skin-sam yui3-skin-sam mydy-dypatil-edu--rait pagelayout-incourse course-5921 context-726956 cmid-606774 category-879 desktopdevice pagewidthnormal categoryicons zoomin two-column  has-region-side-pre used-region-side-pre has-region-footer-left empty-region-footer-left has-region-footer-middle empty-region-footer-middle has-region-footer-right empty-region-footer-right side-pre-only">

<div class="skiplinks"><a class="skip" href="#maincontent">Skip to main content</a></div>
<script type="text/javascript">
//<![CDATA[
document.body.className += ' jsenabled';
//]]>
</script>


<header role="banner">
    <div id="page-header" class="clearfix oldnavbar">
        <div class="container-fluid">
            <div class="row-fluid">
                <!-- HEADER: LOGO AREA -->
                <div class="ecol12 pull-left">
                                            <a class="logo" href="//mydy.dypatil.edu/rait" title="Home"></a>
                    					<nav role="navigation">
						<div class="topnavbar navbar oldnavbar moodle-has-zindex">
							<div class="container-fluid navbar-inner">
								<div class="row-fluid">
									<div class="pull-right">
										<div class="usermenu">
											<ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=z9VmVG5VJO"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>										</div>
										<div class="messagemenu">
											<ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>										</div>
										<div class="messagemenu messagemenu_video">
											<ul class="nav"><li><a class="videotutorial" href="https://mydy.dypatil.edu/rait/mod/page/view.php?id=101">Training Video</a></li></ul>										</div>
										<!--<div class="messagemenu">-->
																					<!--</div>-->
										<!--<div class="messagemenu">-->
																					<!--</div>-->
										<div class="gotobottommenu">
											<ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>										</div>
									</div>
								</div>
							</div>
						</div>
					</nav>
                </div>


            </div>
        </div>
    </div>
    <nav role="navigation">
        <div id='essentialnavbar' class="navbar oldnavbar moodle-has-zindex">
            <div class="container-fluid navbar-inner">
                <div class="row-fluid">
                    <div class="custommenus pull-left">
                        <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </a>
                                            <!--<div class="pull-right">-->
                    <!--    <div class="usermenu">-->
                    <!--        <ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=z9VmVG5VJO"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>-->
                    <!--    </div>-->
                    <!--    <div class="messagemenu">-->
                    <!--        <ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>-->
                    <!--    </div>-->
                    <!--    <div class="messagemenu">-->
                    <!--        <ul class="nav"></ul>-->
                    <!--    </div>-->
                    <!--    <div class="messagemenu">-->
                    <!--        <ul class="nav"></ul>-->
                    <!--    </div>-->
                    <!--    <div class="gotobottommenu">-->
                    <!--        <ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>-->
                    <!--    </div>-->
                    <!--</div>-->
                        <div class="nav-collapse collapse pull-left">
                            <div id="custom_menu_language">
                                <ul class="nav"></ul>                            </div>
                            <div id="custom_menu_courses">
                                <ul class="nav"></ul>                            </div>
                                                        <div id="custom_menu">
                                <ul class="nav"></ul>                            </div>
                            <div id="custom_menu_activitystream">
                                                            </div>
                            <ul class="nav pull-left">
                                                                <li class="hbl"><a href="#" class="moodlezoom"><i class="fa fa-outdent fa-lg"></i> <span class="zoomdesc"></span></a></li>
                                <li class="sbl"><a href="#" class="moodlezoom"><i class="fa fa-indent fa-lg"></i> <span class="zoomdesc"></span></a></li>
                                                             </ul>

                    <!--******************code added by anil-started here*******************-->
							<div id="custom_menu_topmenu">
                                 <!--*********code added by anil*************-->
                                <ul class="nav"><li><a href="https://mydy.dypatil.edu/rait/" class="navbarlinks">Home</a></li><li><a href="http://m.p-y.tm/PUPRTT" class="navbarlinks" target="_blank">Fee Payment</a></li><li><a href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php" class="navbarlinks">Exams</a></li><li><a href="https://mydy.dypatil.edu/rait/local/dypmarket/index.php" id="marketplace">Market Place</a></li></ul>                    <!--******************code added by anil-ended here*******************-->
							</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</header>

<div id="page" class="container-fluid">
    <div id="page-navbar" class="clearfix row-fluid">
        <div
            class="breadcrumb-nav pull-left"><ul class="breadcrumb style2"><li style="z-index:99;"><a href="https://mydy.dypatil.edu/rait/my/">Dashboard</a></li><li style="z-index:98;"><a title="Operating System" href="https://mydy.dypatil.edu/rait/course/view.php?id=5921">CAC403-22-A-AIML</a></li><li style="z-index:97;"><span tabindex="0">General</span></li><li style="z-index:96;"><a title="File" href="https://mydy.dypatil.edu/rait/mod/resource/view.php?id=606774">ebook os</a></li></ul></div>
        <nav
            class="breadcrumb-button pull-right"></nav>
    </div>
    <section role="main-content">
        <!-- Start Main Regions -->
        <div id="page-content" class="row-fluid">
            <div id="region-bs-main-and-pre" class="span12">
                <div class="row-fluid">
                                            <section id="region-main" class="span9 pull-right">
                    <h1 class="coursetitle">Operating System</h1><div class="bor"></div>                                                        <div role="main"><span id="maincontent"></span><h2>ebook os</h2><div class="resourceworkaround">Click <a href="https://mydy.dypatil.edu/rait/pluginfile.php/726956/mod_resource/content/1/Operating_System_Concepts%2C_8th_Edition%5BA4%5D.pdf" >Operating_System_Concepts,_8th_Edition[A4].pdf</a> link to view the file.</div><div id="fb-root"></div><div id="myratings"></div><div id="resource_pages"><div class="like_unlike"><div id="contents_39057" style="float: left;"><div id="label_like_39057" style="float: left; padding: 0 8px 0 0;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;resource&quot;, 606774, 39057, 5921, 0)" /></div><span  id="count_likearea" class="count_likearea_39057"><a id="anchorclass_39057" href="javascript:void(0)" onClick="fnViewAllLikes(39057)">0</a></span><div class="courselike" id="like_list_39057" style="display: none;"><div style="float: right; cursor: pointer;" class="closeicon39057"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="like_closeicon" /></div><span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Likes</b></span><div class="like_39057"></div></div><div id="label_unlike_39057" style="float: left; padding: 0 8px 0 10px; margin-top:5px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Dislike" id="unlikeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;resource&quot;, 606774, 39057, 5921, 1)" /></div><span id="count_unlikearea"  class="count_unlikearea_39057"><a id="anchorclass_39057" href="javascript:void(0)" onClick="fnViewAllunLikes(39057)">0</a></span><div class="courseunlike" id="unlike_list_39057" style="display: none;"><div style="float: right; cursor: pointer;" class="closeicon39057"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="unlike_closeicon" /></div><span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Unlikes</b></span><div class="unlike_39057"></div></div></div></div><div class="radiostars"><div class="overall_ratings_39057" style="float: left; cursor: pointer;"><img title='0 out of 5' src='https://mydy.dypatil.edu/rait/local/ratings/pix/star0.png'  onclick='fnViewAllRatings(5921, 606774, 39057, "resource", "https://mydy.dypatil.edu/rait", "ebook os")'/></div><div class="overall_users">(<font class='totalcount_39057'>0</font> users)</div></div><div class="mycomment"><a id="anchorclass_39057" href="javascript:void(0)" onClick="fnViewAllComments(39057)"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/comment.png" title="Comment" id="custom_icons" /></a>&nbsp;(<font class="commentcount_39057">0</font>)<div class="coursecomment" id="comment_list_39057" style="display: none;"><div style="float: right; cursor: pointer;" class="closeicon39057"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="comment_closeicon" /></div><textarea name="commentarea" id="mycomment_39057" rows="2" cols="50"></textarea><a class="commentclick_39057" href="javascript:void(0)" onClick="fnComment(5921, 606774, 39057, &quot;resource&quot;, &quot;https://mydy.dypatil.edu/rait&quot;)" style="font-size: 12px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/add-comment.gif" /></a><div class="comment_39057"></div></div></div></div></div>                                                    </section>
                    <aside id="block-region-side-pre" class="span3 desktop-first-column block-region" data-blockregion="side-pre" data-droptarget="1"><a href="#sb-1" class="skip-block">Skip My tasks</a><div id="inst19" class="block_universitystructure  block" role="complementary" data-block="universitystructure" data-instanceid="19" aria-labelledby="instance-19-header" data-dockable="1"><div class="header"><div class="title"><div class="block_action"></div><h2 id="instance-19-header">My tasks</h2></div></div><div class="content"><ul class="block_tree list"><li class="type_unknown depth_1 contains_branch simple_invisible"><p class="tree_item branch active_tree_node navigation_node" ><span  ><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span><li class="type_course depth_2 contains_branch"><p class="tree_item branch hasicon active_tree_node" ><span class="usdimmed_text" >My Learnings</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/timetable/calendarview.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">TimeTable Calendar</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/myacademics/transcript.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Transcript</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/academiccalendar"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Academic Calendar</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/feemanagement/studentfeedetails.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Fee Details</a></p></li></ul><li class="type_category depth_3 contains_branch"><p class="tree_item branch active_tree_node" ><span class="usdimmed_text" >Examination</span><ul><li class="type_course depth_4 collapsed contains_branch"><p class="tree_item nomodule hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php">Scheduled Exams</a></p></li><li class="type_course depth_4 collapsed contains_branch"><p class="tree_item nomodule hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/examination/studentresults.php">Student Examsresults </a></p></li></ul></li><li class="type_course depth_3 contains_branch"><p class="tree_item branch hasicon active_tree_node" ><span class="usdimmed_text" >My Profile</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/users/profile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">View Profile</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Edit Profile</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/local/users/change_password.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Change Password</a></p></li></ul></li></ul></li></ul></div></div><span id="sb-1" class="skip-block-to"></span><a href="#sb-3" class="skip-block">Skip Administration</a><div id="inst5" class="block_settings  block" role="navigation" data-block="settings" data-instanceid="5" aria-labelledby="instance-5-header" data-dockable="1"><div class="header"><div class="title"><div class="block_action"></div><h2 id="instance-5-header">Administration</h2></div></div><div class="content"><div id="settingsnav" class="box block_tree_box"><ul class="block_tree list"><li class="type_course collapsed contains_branch" aria-expanded="false"><p class="tree_item branch root_node"><span tabindex="0">Course administration</span></p><ul><li class="type_setting collapsed item_with_icon"><p class="tree_item leaf"><a href="https://mydy.dypatil.edu/rait/grade/report/index.php?id=5921"><i class="fa fa-table icon" title=""><img alt="" class="smallicon navicon" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/grades" /></i>Grades</a></p></li></ul></li></ul></div></div></div><span id="sb-3" class="skip-block-to"></span><a href="#sb-5" class="skip-block">Skip Previous semester classes</a><div id="inst31230" class="block_stu_previousclasses  block" role="complementary" data-block="stu_previousclasses" data-instanceid="31230" aria-labelledby="instance-31230-header" data-dockable="1"><div class="header"><div class="title"><div class="block_action"></div><h2 id="instance-31230-header">Previous semester classes</h2></div></div><div class="content"><ul class="block_tree list"><li class="type_unknown depth_1 contains_branch simple_invisible"><p class="tree_item branch active_tree_node navigation_node" ><span  ><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span><li class="type_course depth_2 contains_branch"><p class="tree_item branch hasiconactive_tree_node" ><span class="usdimmed_text" >Semester I</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4642" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics I</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4643" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Structered Programming</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4644" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Electronics Engineering</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4645" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Physics</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=4646" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">English For Engineers</a></p></li></ul></li><li class="type_course depth_2 collapsed contains_branch"><p class="tree_item branch hasicon" ><span class="usdimmed_text" >Semester II</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5067" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics-II</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5068" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Chemistry II</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5069" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Data Structures</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5071" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Digital Logic Design</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5072" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Environmental Studies</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5070" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Communication Engineering</a></p></li></ul></li><li class="type_course depth_2 collapsed contains_branch"><p class="tree_item branch hasicon" ><span class="usdimmed_text" >Semester III</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5197" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Database Management System</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5198" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Design and Analysis of Algorithms</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5199" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Object Oriented Programming</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5200" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Computer Organization & Architecture</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5201" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Statistical Methods</a></p></li></ul></li><li class="type_course depth_2 collapsed contains_branch"><p class="tree_item branch hasicon" ><span class="usdimmed_text" >Semester IV</span><ul><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5919" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Artificial Intelligence</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5920" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Software Engineering</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5921" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Operating System</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5922" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Programming with Python</a></p></li><li class="contains_branch item_with_icon"><p class="tree_item leaf hasicon" ><a  href="https://mydy.dypatil.edu/rait/course/view.php?id=5923" target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Formal Language Automata Language</a></p></li></ul></li></ul></li></ul></div></div><span id="sb-5" class="skip-block-to"></span></aside>                </div>
                            </div>
        </div>
        <!-- End Main Regions -->
    </section>
</div>

    <footer role="contentinfo" id="page-footer">
        <div class="container-fluid">
                        <div class="row-fluid footerblocks">
                <div class="span8 pull-left footersite-text">
                    <p><h4>'Education is not the learning of many facts </h4></p><p><h4>but the training of the mind to think.' - Albert Einstein</h4></p>
                </div>
                <div class="span4 pull-right footersite-icons">
                                    </div>
            </div>
            <div class="row-fluid footerblocks">
                <div class="span4 pull-left">
                    <div class="column">
                        <aside id="block-region-footer-left" class="block-region" data-blockregion="footer-left" data-droptarget="1"></aside>                    </div>
                </div>
                <div class="span4 center">
                    <div class="column">
                        <aside id="block-region-footer-middle" class="block-region" data-blockregion="footer-middle" data-droptarget="1"></aside>                    </div>
                </div>
                <div class="span4 pull-right">
                    <div class="column">
                        <aside id="block-region-footer-right" class="block-region" data-blockregion="footer-right" data-droptarget="1"></aside>                    </div>
                </div>
            </div>
            <div class="footerlinks row-fluid">
                <hr/>
                <span class="helplink"></span>
                                            </div>
            <div class="footerperformance row-fluid">
                            </div>
            <div class="footercredit row-fluid">
                The Essential theme is developed, enhanced and maintained by <a href="//about.me/gjbarnard" target="_blank">Gareth J Barnard</a>
            </div>
        </div>
    </footer>
    <a href="#top" class="back-to-top" ><i class="fa fa-angle-up "></i></a>
<!--js file commented and included in blocks/events instead of adding in theme footer-->
<!--<script src="https://cdn.rawgit.com/vast-engineering/jquery-popup-overlay/1.7.10/jquery.popupoverlay.js"></script>-->
<script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/custom_zoom.js"></script>
<script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/select2.min.js"></script>
<link href="https://mydy.dypatil.edu/rait/theme/essential/style/select2.min.css" rel="stylesheet" />

    <script type="text/javascript">
        jQuery(document).ready(function () {
            $('#id_cobaltcourseid').select2();
            $('#id_onlinecourseid').select2();
            jQuery('#essentialnavbar').affix({offset: {top: $('#page-header').height()}});$('#page').fitVids();        });
    </script>
<script type="text/javascript">
//<![CDATA[
var require = {
    baseUrl : 'https://mydy.dypatil.edu/rait/lib/requirejs.php/1709815567/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,

    paths: {
        jquery: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/jquery-1.11.2.min',
        jqueryui: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/ui-1.11.4/jquery-ui.min',
        jqueryprivate: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
</script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/require.min.js"></script>
<script type="text/javascript">
//<![CDATA[
require(['core/first'], function() {
;
require(["core/log"], function(amd) { amd.setConfig({"level":"warn"}); });
});
//]]>
</script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/ratings.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/facebook.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/twitter.js"></script>
<script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/footer"></script>
<script type="text/javascript">
//<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","viewallcourses":"View all courses","morehelp":"More help","loadinghelp":"Loading...","cancel":"Cancel","yes":"Yes","confirm":"Confirm","no":"No","areyousure":"Are you sure?","closebuttontitle":"Close","unknownerror":"Unknown error"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source","select":"Select"},"block":{"addtodock":"Move this to the dock","undockitem":"Undock this item","dockblock":"Dock {$a} block","undockblock":"Undock {$a} block","undockall":"Undock all","hidedockpanel":"Hide the dock panel","hidepanel":"Hide panel"},"langconfig":{"thisdirectionvertical":"btt"},"admin":{"confirmation":"Confirmation"}};
//]]>
</script>
<script type="text/javascript">
//<![CDATA[
var navtreeexpansions4 = [{"id":"expandable_branch_30_168117","key":"168117","type":30},{"id":"expandable_branch_30_168118","key":"168118","type":30},{"id":"expandable_branch_30_168119","key":"168119","type":30},{"id":"expandable_branch_30_168120","key":"168120","type":30},{"id":"expandable_branch_30_168121","key":"168121","type":30},{"id":"expandable_branch_30_168122","key":"168122","type":30},{"id":"expandable_branch_30_168123","key":"168123","type":30},{"id":"expandable_branch_30_168124","key":"168124","type":30},{"id":"expandable_branch_30_168125","key":"168125","type":30},{"id":"expandable_branch_30_168126","key":"168126","type":30},{"id":"expandable_branch_30_168477","key":"168477","type":30},{"id":"expandable_branch_30_168478","key":"168478","type":30},{"id":"expandable_branch_30_168479","key":"168479","type":30},{"id":"expandable_branch_0_mycourses","key":"mycourses","type":0}];
//]]>
</script>
<script type="text/javascript">
//<![CDATA[
YUI().use('node', function(Y) {
M.util.load_flowplayer();
setTimeout("fix_column_widths()", 20);
Y.use("moodle-core-dock-loader",function() {M.core.dock.loader.initLoader();
});
Y.use("moodle-theme_essential-zoom",function() {M.theme_essential.zoom.init();
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"19","instance":"19","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"4","instance":"4","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"5","instance":"5","candock":true});
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"31230","instance":"31230","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"en"});
});
M.util.help_popups.setup(Y);
Y.use("moodle-core-popuphelp",function() {M.core.init_popuphelp();
});
M.util.init_block_hider(Y, {"id":"inst19","title":"My tasks","preference":"block19hidden","tooltipVisible":"Hide My tasks block","tooltipHidden":"Show My tasks block"});
M.util.init_block_hider(Y, {"id":"inst5","title":"Administration","preference":"block5hidden","tooltipVisible":"Hide Administration block","tooltipHidden":"Show Administration block"});
M.util.init_block_hider(Y, {"id":"inst31230","title":"Previous semester classes","preference":"block31230hidden","tooltipVisible":"Hide Previous semester classes block","tooltipHidden":"Show Previous semester classes block"});
 M.util.js_pending('random663ba61d42f7c5'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random663ba61d42f7c5'); });

});
//]]>
</script>
</body>
</html>

"""

response4 = """
<!DOCTYPE html>
<html dir="ltr" lang="en" xml:lang="en" class="no-js">

<head>
    <title>CAC403-22-A-AIML: Operating System Virtual Lab</title>
    <link rel="shortcut icon" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/favicon" />
    <link rel="stylesheet"
        href="//mydy.dypatil.edu/rait/pluginfile.php/1/theme_essential/style/1709815567/essential.css">

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="keywords" content="moodle, CAC403-22-A-AIML: Operating System Virtual Lab" />
    <script type="text/javascript">
        //<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/mydy.dypatil.edu\/rait","sesskey":"c5KroZlWWb","loadingicon":"https:\/\/mydy.dypatil.edu\/rait\/theme\/image.php\/essential\/core\/1709815567\/i\/loading_small","themerev":"1709815567","slasharguments":1,"theme":"essential","jsrev":"1709815567","admin":"admin","svgicons":true};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''};if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else me.path=component+'/'+component+'.'+me.type};
YUI_config = {"debug":false,"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?m\/1709815567\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"m\/1709815567\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-checknet":{"requires":["base-base","moodle-core-notification-alert","io-base"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-dock":{"requires":["base","node","event-custom","event-mouseenter","event-resize","escape","moodle-core-dock-loader"]},"moodle-core-dock-loader":{"requires":["escape"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-formautosubmit":{"requires":["base","event-key"]},"moodle-core-formchangechecker":{"requires":["base","event-focus"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core_availability-form":{"requires":["base","node","event","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-calendar-info":{"requires":["base","node","event-mouseenter","event-key","overlay","moodle-calendar-info-skin"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-modchooser":{"requires":["moodle-core-chooserdialogue","moodle-course-coursebase"]},"moodle-course-toolboxes":{"requires":["node","base","event-key","node","io","moodle-course-coursebase","moodle-course-util"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-passwordunmask":{"requires":["node","base"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-showadvanced":{"requires":["node","base","selector-css3"]},"moodle-core_message-messenger":{"requires":["escape","handlebars","io-base","moodle-core-notification-ajaxexception","moodle-core-notification-alert","moodle-core-notification-dialogue","moodle-core-notification-exception"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-qbankmanager":{"requires":["node","selector-css3"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_cohort-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_customcert-rearrange":{"requires":["dd-delegate","dd-drag"]},"moodle-mod_forum-subscriptiontoggle":{"requires":["base-base","io-base"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-quizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-core-notification-dialogue"]},"moodle-mod_quiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_navigation-navigation":{"requires":["base","io-base","node","event-synthetic","event-delegate","json-parse"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-format_grid-gridkeys":{"requires":["event-nav-keys"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_html-button":{"requires":["moodle-editor_atto-plugin","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1709815567\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.mathjax.org\/mathjax\/2.5-latest\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js&amp;rollup/1709815567/mcore-min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/jquery-1.11.2.min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/ui-1.11.4/jquery-ui.min.js">
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/bootstrap_2_3_2_min.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/jBreadCrumb_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/fitvids_1_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/anti_gravity_1_1.js"></script>
    <script id="firstthemesheet" type="text/css">
        /** Required in order to fix style inclusion problems in IE with YUI **/
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/styles.php/essential/1709815567/all" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/jquery-ui.css" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/style.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/javascript-static.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/head">
    </script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google web fonts -->
    <!--<link href='http://fonts.googleapis.com/css?family=Domine' rel='stylesheet' type='text/css'>-->
    <!-- iOS Homescreen Icons -->

    <link rel="apple-touch-icon-precomposed" sizes="57x57"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone_retina" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad_retina" />
    <!-- Start Analytics -->
    <!-- End Analytics -->

    <!--include custom fonts-->
    <style>
        @font-face {
            font-family: "Minion Pro Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/Minion-Pro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Light";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Light.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Semibold";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Semibold.ttf');
        }
    </style>

    <script type="text/javascript">
        $(document).ready(function() {
	  	//var $pwidth = $(window).width();
			//var $loggedin = $('body').hasClass('loggedin');

			/*if($pwidth >= 768){
				$('.offcanvas, #content-container').addClass('active');
			}*/

		  $('[data-toggle=offcanvas]').click(function() {

		  var $pwidth = $(window).width();
			$('.offcanvas').toggleClass('active');
			$('#content-container').toggleClass('active');

			//do this when in nmobile view
			var $main = $('main').hasClass('active');
			if($pwidth <= 480 ){

				if( $main == true){
					$('body, html').addClass('noscroll');
				}else{
					$('body, html').removeClass('noscroll');
				}
			}

			//do this when in tab/desktop view
			if($pwidth >= 481 ){

				//var $main = $('main').hasClass('active');

				if( $main == false){
					$('body, html').removeClass('noscroll');
				}
			}

		  });
        });
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS starts here -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-62316529-3"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag("js", new Date());
            gtag("config", "UA-62316529-3");
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS ends here -->
</head>

<body id="page-mod-url-view"
    class="format-topcoll  path-mod path-mod-url dir-ltr lang-en yui-skin-sam yui3-skin-sam mydy-dypatil-edu--rait pagelayout-incourse course-5921 context-726954 cmid-606772 category-879 desktopdevice pagewidthnormal categoryicons zoomin two-column  has-region-side-pre used-region-side-pre has-region-footer-left empty-region-footer-left has-region-footer-middle empty-region-footer-middle has-region-footer-right empty-region-footer-right side-pre-only">

    <div class="skiplinks"><a class="skip" href="#maincontent">Skip to main content</a></div>
    <script type="text/javascript">
        //<![CDATA[
document.body.className += ' jsenabled';
//]]>
    </script>


    <header role="banner">
        <div id="page-header" class="clearfix oldnavbar">
            <div class="container-fluid">
                <div class="row-fluid">
                    <!-- HEADER: LOGO AREA -->
                    <div class="ecol12 pull-left">
                        <a class="logo" href="//mydy.dypatil.edu/rait" title="Home"></a>
                        <nav role="navigation">
                            <div class="topnavbar navbar oldnavbar moodle-has-zindex">
                                <div class="container-fluid navbar-inner">
                                    <div class="row-fluid">
                                        <div class="pull-right">
                                            <div class="usermenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a class="dropdown-toggle"
                                                            data-toggle="dropdown"
                                                            href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu pull-right">
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a>
                                                            </li>
                                                            <li class="dropdown-submenu preferences"><a
                                                                    class="dropdown-toggle" data-toggle="dropdown"
                                                                    href="#"><em><i class="fa fa-cog"></i>Preferences</em></a>
                                                                <ul class="dropdown-menu">
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a>
                                                                    </li>
                                                                </ul>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a>
                                                            </li>
                                                            <li><a target=""
                                                                    href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="messagemenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a
                                                            href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations"
                                                            class="dropdown-toggle" data-toggle="dropdown"
                                                            title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu">
                                                            <li><a title="You have submitted your assignment submission for Vlab - ER modeling"
                                                                    href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950">
                                                                    <div class="notification read">
                                                                        <i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span>
                                                                    </div>
                                                                </a>
                                                        </ul>
                                                </ul>
                                            </div>
                                            <div class="messagemenu messagemenu_video">
                                                <ul class="nav">
                                                    <li><a class="videotutorial"
                                                            href="https://mydy.dypatil.edu/rait/mod/page/view.php?id=101">Training
                                                            Video</a></li>
                                                </ul>
                                            </div>
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <div class="gotobottommenu">
                                                <ul class="nav">
                                                    <li><a title="Go to the bottom of the page"
                                                            href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </nav>
                    </div>


                </div>
            </div>
        </div>
        <nav role="navigation">
            <div id='essentialnavbar' class="navbar oldnavbar moodle-has-zindex">
                <div class="container-fluid navbar-inner">
                    <div class="row-fluid">
                        <div class="custommenus pull-left">
                            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </a>
                            <!--<div class="pull-right">-->
                            <!--    <div class="usermenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="gotobottommenu">-->
                            <!--        <ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>-->
                            <!--    </div>-->
                            <!--</div>-->
                            <div class="nav-collapse collapse pull-left">
                                <div id="custom_menu_language">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_courses">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_activitystream">
                                </div>
                                <ul class="nav pull-left">
                                    <li class="hbl"><a href="#" class="moodlezoom"><i class="fa fa-outdent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                    <li class="sbl"><a href="#" class="moodlezoom"><i class="fa fa-indent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                </ul>

                                <!--******************code added by anil-started here*******************-->
                                <div id="custom_menu_topmenu">
                                    <!--*********code added by anil*************-->
                                    <ul class="nav">
                                        <li><a href="https://mydy.dypatil.edu/rait/" class="navbarlinks">Home</a></li>
                                        <li><a href="http://m.p-y.tm/PUPRTT" class="navbarlinks" target="_blank">Fee
                                                Payment</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php"
                                                class="navbarlinks">Exams</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/dypmarket/index.php"
                                                id="marketplace">Market Place</a></li>
                                    </ul>
                                    <!--******************code added by anil-ended here*******************-->
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <div id="page" class="container-fluid">
        <div id="page-navbar" class="clearfix row-fluid">
            <div class="breadcrumb-nav pull-left">
                <ul class="breadcrumb style2">
                    <li style="z-index:99;"><a href="https://mydy.dypatil.edu/rait/my/">Dashboard</a></li>
                    <li style="z-index:98;"><a title="Operating System"
                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921">CAC403-22-A-AIML</a></li>
                    <li style="z-index:97;"><span tabindex="0">General</span></li>
                    <li style="z-index:96;"><a title="Reference URL"
                            href="https://mydy.dypatil.edu/rait/mod/url/view.php?id=606772">Operating System Virtual
                            Lab</a></li>
                </ul>
            </div>
            <nav class="breadcrumb-button pull-right"></nav>
        </div>
        <section role="main-content">
            <!-- Start Main Regions -->
            <div id="page-content" class="row-fluid">
                <div id="region-bs-main-and-pre" class="span12">
                    <div class="row-fluid">
                        <section id="region-main" class="span9 pull-right">
                            <h1 class="coursetitle">Operating System</h1>
                            <div class="bor"></div>
                            <div role="main"><span id="maincontent"></span>
                                <h2>Operating System Virtual Lab</h2>
                                <div class="urlworkaround">Click <a
                                        href="https://hansalshah007.github.io/osvirtuallab/">https://hansalshah007.github.io/osvirtuallab/</a>
                                    link to open resource.</div>
                                <div id="fb-root"></div>
                                <div id="myratings"></div>
                                <div id="resource_pages">
                                    <div class="like_unlike">
                                        <div id="contents_189574" style="float: left;">
                                            <div id="label_like_189574" style="float: left; padding: 0 8px 0 0;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;url&quot;, 606772, 189574, 5921, 0)" />
                                            </div>
                                            <span  id="count_likearea" class="count_likearea_189574"><a id="anchorclass_189574" href="javascript:void(0)" onClick="fnViewAllLikes(189574)">0</a></span>
                                            <div class="courselike" id="like_list_189574" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon189574"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="like_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Likes</b></span>
                                                <div class="like_189574"></div>
                                            </div>
                                            <div id="label_unlike_189574"
                                                style="float: left; padding: 0 8px 0 10px; margin-top:5px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Dislike" id="unlikeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;url&quot;, 606772, 189574, 5921, 1)" />
                                            </div>
                                            <span id="count_unlikearea"  class="count_unlikearea_189574"><a id="anchorclass_189574" href="javascript:void(0)" onClick="fnViewAllunLikes(189574)">0</a></span>
                                            <div class="courseunlike" id="unlike_list_189574" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon189574"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="unlike_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Unlikes</b></span>
                                                <div class="unlike_189574"></div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="radiostars">
                                        <div class="overall_ratings_189574" style="float: left; cursor: pointer;"><img title='0 out of 5' src='https://mydy.dypatil.edu/rait/local/ratings/pix/star0.png'  onclick='fnViewAllRatings(5921, 606772, 189574, "url", "https://mydy.dypatil.edu/rait", "Operating System Virtual Lab")'/>
                                        </div>
                                        <div class="overall_users">(<font class='totalcount_189574'>0</font> users)
                                        </div>
                                    </div>
                                    <div class="mycomment"><a id="anchorclass_189574" href="javascript:void(0)"
                                            onClick="fnViewAllComments(189574)"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/comment.png" title="Comment" id="custom_icons" /></a>&nbsp;(
                                        <font class="commentcount_189574">0</font>)<div class="coursecomment"
                                            id="comment_list_189574" style="display: none;">
                                            <div style="float: right; cursor: pointer;" class="closeicon189574"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="comment_closeicon" />
                                            </div>
                                            <textarea name="commentarea" id="mycomment_189574" rows="2" cols="50"></textarea><a
                                                class="commentclick_189574" href="javascript:void(0)"
                                                onClick="fnComment(5921, 606772, 189574, &quot;url&quot;, &quot;https://mydy.dypatil.edu/rait&quot;)"
                                                style="font-size: 12px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/add-comment.gif" /></a>
                                            <div class="comment_189574"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <aside id="block-region-side-pre" class="span3 desktop-first-column block-region"
                            data-blockregion="side-pre" data-droptarget="1"><a href="#sb-1" class="skip-block">Skip My
                                tasks</a>
                            <div id="inst19" class="block_universitystructure  block" role="complementary"
                                data-block="universitystructure" data-instanceid="19"
                                aria-labelledby="instance-19-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-19-header">My tasks</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Learnings</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/timetable/calendarview.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">TimeTable Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/myacademics/transcript.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Transcript</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/academiccalendar"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Academic Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/feemanagement/studentfeedetails.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Fee Details</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        <li class="type_category depth_3 contains_branch">
                                            <p class="tree_item branch active_tree_node">
                                                <span class="usdimmed_text" >Examination</span>
                                            <ul>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php">Scheduled
                                                            Exams</a></p>
                                                </li>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/studentresults.php">Student
                                                            Examsresults </a></p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_3 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Profile</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/profile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">View Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Edit Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/change_password.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Change Password</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-1" class="skip-block-to"></span><a href="#sb-3" class="skip-block">Skip
                                Administration</a>
                            <div id="inst5" class="block_settings  block" role="navigation" data-block="settings"
                                data-instanceid="5" aria-labelledby="instance-5-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-5-header">Administration</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <div id="settingsnav" class="box block_tree_box">
                                        <ul class="block_tree list">
                                            <li class="type_course collapsed contains_branch" aria-expanded="false">
                                                <p class="tree_item branch root_node">
                                                    <span tabindex="0">Course administration</span></p>
                                                <ul>
                                                    <li class="type_setting collapsed item_with_icon">
                                                        <p class="tree_item leaf"><a
                                                                href="https://mydy.dypatil.edu/rait/grade/report/index.php?id=5921"><i class="fa fa-table icon" title=""><img alt="" class="smallicon navicon" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/grades" /></i>Grades</a>
                                                        </p>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div><span id="sb-3" class="skip-block-to"></span><a href="#sb-5" class="skip-block">Skip
                                Previous semester classes</a>
                            <div id="inst31230" class="block_stu_previousclasses  block" role="complementary"
                                data-block="stu_previousclasses" data-instanceid="31230"
                                aria-labelledby="instance-31230-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-31230-header">Previous semester classes</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasiconactive_tree_node">
                                                <span class="usdimmed_text" >Semester I</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4642"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics I</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4643"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Structered Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4644"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Electronics Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4645"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Physics</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4646"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">English For Engineers</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester II</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5067"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics-II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5068"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Chemistry II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5069"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Data Structures</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5071"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Digital Logic Design</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5072"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Environmental Studies</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5070"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Communication Engineering</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester III</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5197"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Database Management System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5198"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Design and Analysis of Algorithms</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5199"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Object Oriented Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5200"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Computer Organization & Architecture</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5201"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Statistical Methods</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester IV</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5919"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Artificial Intelligence</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5920"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Software Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Operating System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Programming with Python</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5923"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Formal Language Automata Language</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-5" class="skip-block-to"></span>
                        </aside>
                    </div>
                </div>
            </div>
            <!-- End Main Regions -->
        </section>
    </div>

    <footer role="contentinfo" id="page-footer">
        <div class="container-fluid">
            <div class="row-fluid footerblocks">
                <div class="span8 pull-left footersite-text">
                    <p>
                    <h4>'Education is not the learning of many facts </h4>
                    </p>
                    <p>
                    <h4>but the training of the mind to think.' - Albert Einstein</h4>
                    </p>
                </div>
                <div class="span4 pull-right footersite-icons">
                </div>
            </div>
            <div class="row-fluid footerblocks">
                <div class="span4 pull-left">
                    <div class="column">
                        <aside id="block-region-footer-left" class="block-region" data-blockregion="footer-left"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 center">
                    <div class="column">
                        <aside id="block-region-footer-middle" class="block-region" data-blockregion="footer-middle"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 pull-right">
                    <div class="column">
                        <aside id="block-region-footer-right" class="block-region" data-blockregion="footer-right"
                            data-droptarget="1"></aside>
                    </div>
                </div>
            </div>
            <div class="footerlinks row-fluid">
                <hr />
                <span class="helplink"></span>
            </div>
            <div class="footerperformance row-fluid">
            </div>
            <div class="footercredit row-fluid">
                The Essential theme is developed, enhanced and maintained by <a href="//about.me/gjbarnard"
                    target="_blank">Gareth J Barnard</a>
            </div>
        </div>
    </footer>
    <a href="#top" class="back-to-top"><i class="fa fa-angle-up "></i></a>
    <!--js file commented and included in blocks/events instead of adding in theme footer-->
    <!--<script src="https://cdn.rawgit.com/vast-engineering/jquery-popup-overlay/1.7.10/jquery.popupoverlay.js"></script>-->
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/custom_zoom.js"></script>
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/select2.min.js"></script>
    <link href="https://mydy.dypatil.edu/rait/theme/essential/style/select2.min.css" rel="stylesheet" />

    <script type="text/javascript">
        jQuery(document).ready(function () {
            $('#id_cobaltcourseid').select2();
            $('#id_onlinecourseid').select2();
            jQuery('#essentialnavbar').affix({offset: {top: $('#page-header').height()}});$('#page').fitVids();        });
    </script>
    <script type="text/javascript">
        //<![CDATA[
var require = {
    baseUrl : 'https://mydy.dypatil.edu/rait/lib/requirejs.php/1709815567/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,

    paths: {
        jquery: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/jquery-1.11.2.min',
        jqueryui: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/ui-1.11.4/jquery-ui.min',
        jqueryprivate: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/require.min.js"></script>
    <script type="text/javascript">
        //<![CDATA[
require(['core/first'], function() {
;
require(["core/log"], function(amd) { amd.setConfig({"level":"warn"}); });
});
//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/ratings.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/facebook.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/twitter.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/footer">
    </script>
    <script type="text/javascript">
        //<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","viewallcourses":"View all courses","morehelp":"More help","loadinghelp":"Loading...","cancel":"Cancel","yes":"Yes","confirm":"Confirm","no":"No","areyousure":"Are you sure?","closebuttontitle":"Close","unknownerror":"Unknown error"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source","select":"Select"},"block":{"addtodock":"Move this to the dock","undockitem":"Undock this item","dockblock":"Dock {$a} block","undockblock":"Undock {$a} block","undockall":"Undock all","hidedockpanel":"Hide the dock panel","hidepanel":"Hide panel"},"langconfig":{"thisdirectionvertical":"btt"},"admin":{"confirmation":"Confirmation"}};
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
var navtreeexpansions4 = [{"id":"expandable_branch_30_168117","key":"168117","type":30},{"id":"expandable_branch_30_168118","key":"168118","type":30},{"id":"expandable_branch_30_168119","key":"168119","type":30},{"id":"expandable_branch_30_168120","key":"168120","type":30},{"id":"expandable_branch_30_168121","key":"168121","type":30},{"id":"expandable_branch_30_168122","key":"168122","type":30},{"id":"expandable_branch_30_168123","key":"168123","type":30},{"id":"expandable_branch_30_168124","key":"168124","type":30},{"id":"expandable_branch_30_168125","key":"168125","type":30},{"id":"expandable_branch_30_168126","key":"168126","type":30},{"id":"expandable_branch_30_168477","key":"168477","type":30},{"id":"expandable_branch_30_168478","key":"168478","type":30},{"id":"expandable_branch_30_168479","key":"168479","type":30},{"id":"expandable_branch_0_mycourses","key":"mycourses","type":0}];
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
YUI().use('node', function(Y) {
M.util.load_flowplayer();
setTimeout("fix_column_widths()", 20);
Y.use("moodle-core-dock-loader",function() {M.core.dock.loader.initLoader();
});
Y.use("moodle-theme_essential-zoom",function() {M.theme_essential.zoom.init();
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"19","instance":"19","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"4","instance":"4","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"5","instance":"5","candock":true});
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"31230","instance":"31230","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"en"});
});
M.util.help_popups.setup(Y);
Y.use("moodle-core-popuphelp",function() {M.core.init_popuphelp();
});
M.util.init_block_hider(Y, {"id":"inst19","title":"My tasks","preference":"block19hidden","tooltipVisible":"Hide My tasks block","tooltipHidden":"Show My tasks block"});
M.util.init_block_hider(Y, {"id":"inst5","title":"Administration","preference":"block5hidden","tooltipVisible":"Hide Administration block","tooltipHidden":"Show Administration block"});
M.util.init_block_hider(Y, {"id":"inst31230","title":"Previous semester classes","preference":"block31230hidden","tooltipVisible":"Hide Previous semester classes block","tooltipHidden":"Show Previous semester classes block"});
 M.util.js_pending('random663baed973cc55'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random663baed973cc55'); });

});
//]]>
    </script>
</body>

</html>
"""

response5 = """
<!DOCTYPE html>
<html dir="ltr" lang="en" xml:lang="en" class="no-js">

<head>
    <title>CAC403-22-A-AIML: IA-II Set 2</title>
    <link rel="shortcut icon" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/favicon" />
    <link rel="stylesheet"
        href="//mydy.dypatil.edu/rait/pluginfile.php/1/theme_essential/style/1709815567/essential.css">

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="keywords" content="moodle, CAC403-22-A-AIML: IA-II Set 2" />
    <script type="text/javascript">
        //<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/mydy.dypatil.edu\/rait","sesskey":"c5KroZlWWb","loadingicon":"https:\/\/mydy.dypatil.edu\/rait\/theme\/image.php\/essential\/core\/1709815567\/i\/loading_small","themerev":"1709815567","slasharguments":1,"theme":"essential","jsrev":"1709815567","admin":"admin","svgicons":true};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''};if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else me.path=component+'/'+component+'.'+me.type};
YUI_config = {"debug":false,"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?m\/1709815567\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"m\/1709815567\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-checknet":{"requires":["base-base","moodle-core-notification-alert","io-base"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-dock":{"requires":["base","node","event-custom","event-mouseenter","event-resize","escape","moodle-core-dock-loader"]},"moodle-core-dock-loader":{"requires":["escape"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-formautosubmit":{"requires":["base","event-key"]},"moodle-core-formchangechecker":{"requires":["base","event-focus"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core_availability-form":{"requires":["base","node","event","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-calendar-info":{"requires":["base","node","event-mouseenter","event-key","overlay","moodle-calendar-info-skin"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-modchooser":{"requires":["moodle-core-chooserdialogue","moodle-course-coursebase"]},"moodle-course-toolboxes":{"requires":["node","base","event-key","node","io","moodle-course-coursebase","moodle-course-util"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-passwordunmask":{"requires":["node","base"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-showadvanced":{"requires":["node","base","selector-css3"]},"moodle-core_message-messenger":{"requires":["escape","handlebars","io-base","moodle-core-notification-ajaxexception","moodle-core-notification-alert","moodle-core-notification-dialogue","moodle-core-notification-exception"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-qbankmanager":{"requires":["node","selector-css3"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_cohort-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_customcert-rearrange":{"requires":["dd-delegate","dd-drag"]},"moodle-mod_forum-subscriptiontoggle":{"requires":["base-base","io-base"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-quizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-core-notification-dialogue"]},"moodle-mod_quiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_navigation-navigation":{"requires":["base","io-base","node","event-synthetic","event-delegate","json-parse"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-format_grid-gridkeys":{"requires":["event-nav-keys"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_html-button":{"requires":["moodle-editor_atto-plugin","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1709815567\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.mathjax.org\/mathjax\/2.5-latest\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js&amp;rollup/1709815567/mcore-min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/jquery-1.11.2.min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/ui-1.11.4/jquery-ui.min.js">
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/bootstrap_2_3_2_min.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/jBreadCrumb_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/fitvids_1_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/anti_gravity_1_1.js"></script>
    <script id="firstthemesheet" type="text/css">
        /** Required in order to fix style inclusion problems in IE with YUI **/
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/styles.php/essential/1709815567/all" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/jquery-ui.css" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/style.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/javascript-static.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/head">
    </script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google web fonts -->
    <!--<link href='http://fonts.googleapis.com/css?family=Domine' rel='stylesheet' type='text/css'>-->
    <!-- iOS Homescreen Icons -->

    <link rel="apple-touch-icon-precomposed" sizes="57x57"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone_retina" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad_retina" />
    <!-- Start Analytics -->
    <!-- End Analytics -->

    <!--include custom fonts-->
    <style>
        @font-face {
            font-family: "Minion Pro Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/Minion-Pro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Light";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Light.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Semibold";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Semibold.ttf');
        }
    </style>

    <script type="text/javascript">
        $(document).ready(function() {
	  	//var $pwidth = $(window).width();
			//var $loggedin = $('body').hasClass('loggedin');

			/*if($pwidth >= 768){
				$('.offcanvas, #content-container').addClass('active');
			}*/

		  $('[data-toggle=offcanvas]').click(function() {

		  var $pwidth = $(window).width();
			$('.offcanvas').toggleClass('active');
			$('#content-container').toggleClass('active');

			//do this when in nmobile view
			var $main = $('main').hasClass('active');
			if($pwidth <= 480 ){

				if( $main == true){
					$('body, html').addClass('noscroll');
				}else{
					$('body, html').removeClass('noscroll');
				}
			}

			//do this when in tab/desktop view
			if($pwidth >= 481 ){

				//var $main = $('main').hasClass('active');

				if( $main == false){
					$('body, html').removeClass('noscroll');
				}
			}

		  });
        });
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS starts here -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-62316529-3"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag("js", new Date());
            gtag("config", "UA-62316529-3");
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS ends here -->
</head>

<body id="page-mod-questionpaper-view"
    class="format-topcoll  path-mod path-mod-questionpaper dir-ltr lang-en yui-skin-sam yui3-skin-sam mydy-dypatil-edu--rait pagelayout-incourse course-5921 context-730443 cmid-610189 category-879 desktopdevice pagewidthnormal categoryicons zoomin two-column  has-region-side-pre used-region-side-pre has-region-footer-left empty-region-footer-left has-region-footer-middle empty-region-footer-middle has-region-footer-right empty-region-footer-right side-pre-only">

    <div class="skiplinks"><a class="skip" href="#maincontent">Skip to main content</a></div>
    <script type="text/javascript">
        //<![CDATA[
document.body.className += ' jsenabled';
//]]>
    </script>


    <header role="banner">
        <div id="page-header" class="clearfix oldnavbar">
            <div class="container-fluid">
                <div class="row-fluid">
                    <!-- HEADER: LOGO AREA -->
                    <div class="ecol12 pull-left">
                        <a class="logo" href="//mydy.dypatil.edu/rait" title="Home"></a>
                        <nav role="navigation">
                            <div class="topnavbar navbar oldnavbar moodle-has-zindex">
                                <div class="container-fluid navbar-inner">
                                    <div class="row-fluid">
                                        <div class="pull-right">
                                            <div class="usermenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a class="dropdown-toggle"
                                                            data-toggle="dropdown"
                                                            href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu pull-right">
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a>
                                                            </li>
                                                            <li class="dropdown-submenu preferences"><a
                                                                    class="dropdown-toggle" data-toggle="dropdown"
                                                                    href="#"><em><i class="fa fa-cog"></i>Preferences</em></a>
                                                                <ul class="dropdown-menu">
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a>
                                                                    </li>
                                                                </ul>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a>
                                                            </li>
                                                            <li><a target=""
                                                                    href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="messagemenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a
                                                            href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations"
                                                            class="dropdown-toggle" data-toggle="dropdown"
                                                            title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu">
                                                            <li><a title="You have submitted your assignment submission for Vlab - ER modeling"
                                                                    href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950">
                                                                    <div class="notification read">
                                                                        <i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span>
                                                                    </div>
                                                                </a>
                                                        </ul>
                                                </ul>
                                            </div>
                                            <div class="messagemenu messagemenu_video">
                                                <ul class="nav">
                                                    <li><a class="videotutorial"
                                                            href="https://mydy.dypatil.edu/rait/mod/page/view.php?id=101">Training
                                                            Video</a></li>
                                                </ul>
                                            </div>
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <div class="gotobottommenu">
                                                <ul class="nav">
                                                    <li><a title="Go to the bottom of the page"
                                                            href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </nav>
                    </div>


                </div>
            </div>
        </div>
        <nav role="navigation">
            <div id='essentialnavbar' class="navbar oldnavbar moodle-has-zindex">
                <div class="container-fluid navbar-inner">
                    <div class="row-fluid">
                        <div class="custommenus pull-left">
                            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </a>
                            <!--<div class="pull-right">-->
                            <!--    <div class="usermenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="gotobottommenu">-->
                            <!--        <ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>-->
                            <!--    </div>-->
                            <!--</div>-->
                            <div class="nav-collapse collapse pull-left">
                                <div id="custom_menu_language">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_courses">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_activitystream">
                                </div>
                                <ul class="nav pull-left">
                                    <li class="hbl"><a href="#" class="moodlezoom"><i class="fa fa-outdent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                    <li class="sbl"><a href="#" class="moodlezoom"><i class="fa fa-indent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                </ul>

                                <!--******************code added by anil-started here*******************-->
                                <div id="custom_menu_topmenu">
                                    <!--*********code added by anil*************-->
                                    <ul class="nav">
                                        <li><a href="https://mydy.dypatil.edu/rait/" class="navbarlinks">Home</a></li>
                                        <li><a href="http://m.p-y.tm/PUPRTT" class="navbarlinks" target="_blank">Fee
                                                Payment</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php"
                                                class="navbarlinks">Exams</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/dypmarket/index.php"
                                                id="marketplace">Market Place</a></li>
                                    </ul>
                                    <!--******************code added by anil-ended here*******************-->
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <div id="page" class="container-fluid">
        <div id="page-navbar" class="clearfix row-fluid">
            <div class="breadcrumb-nav pull-left">
                <ul class="breadcrumb style2">
                    <li style="z-index:99;"><a href="https://mydy.dypatil.edu/rait/my/">Dashboard</a></li>
                    <li style="z-index:98;"><a title="Operating System"
                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921">CAC403-22-A-AIML</a></li>
                    <li style="z-index:97;"><span tabindex="0">IA1  Question bank</span></li>
                    <li style="z-index:96;"><a title="Question Paper"
                            href="https://mydy.dypatil.edu/rait/mod/questionpaper/view.php?id=610189">IA-II Set 2</a>
                    </li>
                </ul>
            </div>
            <nav class="breadcrumb-button pull-right"></nav>
        </div>
        <section role="main-content">
            <!-- Start Main Regions -->
            <div id="page-content" class="row-fluid">
                <div id="region-bs-main-and-pre" class="span12">
                    <div class="row-fluid">
                        <section id="region-main" class="span9 pull-right">
                            <h1 class="coursetitle">Operating System</h1>
                            <div class="bor"></div>
                            <div role="main"><span id="maincontent"></span>
                                <h2>IA-II Set 2</h2>
                                <div class="questionpapercontent questionpapergeneral">
                                    <iframe id="questionpaperobject"
                                        src="https://mydy.dypatil.edu/rait/pluginfile.php/730443/mod_questionpaper/content/1/OS_Question%20Paper_IA-II_EVEN_2023-24_SE_SET-2.docx">
                                        Click <a
                                            href="https://mydy.dypatil.edu/rait/pluginfile.php/730443/mod_questionpaper/content/1/OS_Question%20Paper_IA-II_EVEN_2023-24_SE_SET-2.docx">OS_Question
                                            Paper_IA-II_EVEN_2023-24_SE_SET-2.docx</a> link to view the question paper.
                                    </iframe>
                                </div>
                                <div id="fb-root"></div>
                                <div id="myratings"></div>
                                <div id="questionpaper_pages">
                                    <div class="like_unlike">
                                        <div id="contents_13559" style="float: left;">
                                            <div id="label_like_13559" style="float: left; padding: 0 8px 0 0;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;questionpaper&quot;, 610189, 13559, 5921, 0)" />
                                            </div>
                                            <span  id="count_likearea" class="count_likearea_13559"><a id="anchorclass_13559" href="javascript:void(0)" onClick="fnViewAllLikes(13559)">0</a></span>
                                            <div class="courselike" id="like_list_13559" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon13559"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="like_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Likes</b></span>
                                                <div class="like_13559"></div>
                                            </div>
                                            <div id="label_unlike_13559"
                                                style="float: left; padding: 0 8px 0 10px; margin-top:5px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Dislike" id="unlikeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;questionpaper&quot;, 610189, 13559, 5921, 1)" />
                                            </div>
                                            <span id="count_unlikearea"  class="count_unlikearea_13559"><a id="anchorclass_13559" href="javascript:void(0)" onClick="fnViewAllunLikes(13559)">0</a></span>
                                            <div class="courseunlike" id="unlike_list_13559" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon13559"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="unlike_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Unlikes</b></span>
                                                <div class="unlike_13559"></div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="radiostars">
                                        <div class="overall_ratings_13559" style="float: left; cursor: pointer;"><img title='0 out of 5' src='https://mydy.dypatil.edu/rait/local/ratings/pix/star0.png'  onclick='fnViewAllRatings(5921, 610189, 13559, "questionpaper", "https://mydy.dypatil.edu/rait", "IA-II Set 2")'/>
                                        </div>
                                        <div class="overall_users">(<font class='totalcount_13559'>0</font> users)</div>
                                    </div>
                                    <div class="mycomment"><a id="anchorclass_13559" href="javascript:void(0)"
                                            onClick="fnViewAllComments(13559)"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/comment.png" title="Comment" id="custom_icons" /></a>&nbsp;(
                                        <font class="commentcount_13559">0</font>)<div class="coursecomment"
                                            id="comment_list_13559" style="display: none;">
                                            <div style="float: right; cursor: pointer;" class="closeicon13559"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="comment_closeicon" />
                                            </div>
                                            <textarea name="commentarea" id="mycomment_13559" rows="2" cols="50"></textarea><a
                                                class="commentclick_13559" href="javascript:void(0)"
                                                onClick="fnComment(5921, 610189, 13559, &quot;questionpaper&quot;, &quot;https://mydy.dypatil.edu/rait&quot;)"
                                                style="font-size: 12px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/add-comment.gif" /></a>
                                            <div class="comment_13559"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <aside id="block-region-side-pre" class="span3 desktop-first-column block-region"
                            data-blockregion="side-pre" data-droptarget="1"><a href="#sb-1" class="skip-block">Skip My
                                tasks</a>
                            <div id="inst19" class="block_universitystructure  block" role="complementary"
                                data-block="universitystructure" data-instanceid="19"
                                aria-labelledby="instance-19-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-19-header">My tasks</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Learnings</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/timetable/calendarview.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">TimeTable Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/myacademics/transcript.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Transcript</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/academiccalendar"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Academic Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/feemanagement/studentfeedetails.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Fee Details</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        <li class="type_category depth_3 contains_branch">
                                            <p class="tree_item branch active_tree_node">
                                                <span class="usdimmed_text" >Examination</span>
                                            <ul>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php">Scheduled
                                                            Exams</a></p>
                                                </li>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/studentresults.php">Student
                                                            Examsresults </a></p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_3 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Profile</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/profile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">View Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Edit Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/change_password.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Change Password</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-1" class="skip-block-to"></span><a href="#sb-3" class="skip-block">Skip
                                Administration</a>
                            <div id="inst5" class="block_settings  block" role="navigation" data-block="settings"
                                data-instanceid="5" aria-labelledby="instance-5-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-5-header">Administration</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <div id="settingsnav" class="box block_tree_box">
                                        <ul class="block_tree list">
                                            <li class="type_course collapsed contains_branch" aria-expanded="false">
                                                <p class="tree_item branch root_node">
                                                    <span tabindex="0">Course administration</span></p>
                                                <ul>
                                                    <li class="type_setting collapsed item_with_icon">
                                                        <p class="tree_item leaf"><a
                                                                href="https://mydy.dypatil.edu/rait/grade/report/index.php?id=5921"><i class="fa fa-table icon" title=""><img alt="" class="smallicon navicon" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/grades" /></i>Grades</a>
                                                        </p>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div><span id="sb-3" class="skip-block-to"></span><a href="#sb-5" class="skip-block">Skip
                                Previous semester classes</a>
                            <div id="inst31230" class="block_stu_previousclasses  block" role="complementary"
                                data-block="stu_previousclasses" data-instanceid="31230"
                                aria-labelledby="instance-31230-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-31230-header">Previous semester classes</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasiconactive_tree_node">
                                                <span class="usdimmed_text" >Semester I</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4642"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics I</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4643"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Structered Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4644"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Electronics Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4645"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Physics</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4646"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">English For Engineers</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester II</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5067"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics-II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5068"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Chemistry II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5069"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Data Structures</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5071"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Digital Logic Design</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5072"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Environmental Studies</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5070"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Communication Engineering</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester III</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5197"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Database Management System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5198"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Design and Analysis of Algorithms</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5199"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Object Oriented Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5200"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Computer Organization & Architecture</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5201"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Statistical Methods</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester IV</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5919"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Artificial Intelligence</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5920"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Software Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Operating System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Programming with Python</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5923"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Formal Language Automata Language</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-5" class="skip-block-to"></span>
                        </aside>
                    </div>
                </div>
            </div>
            <!-- End Main Regions -->
        </section>
    </div>

    <footer role="contentinfo" id="page-footer">
        <div class="container-fluid">
            <div class="row-fluid footerblocks">
                <div class="span8 pull-left footersite-text">
                    <p>
                    <h4>'Education is not the learning of many facts </h4>
                    </p>
                    <p>
                    <h4>but the training of the mind to think.' - Albert Einstein</h4>
                    </p>
                </div>
                <div class="span4 pull-right footersite-icons">
                </div>
            </div>
            <div class="row-fluid footerblocks">
                <div class="span4 pull-left">
                    <div class="column">
                        <aside id="block-region-footer-left" class="block-region" data-blockregion="footer-left"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 center">
                    <div class="column">
                        <aside id="block-region-footer-middle" class="block-region" data-blockregion="footer-middle"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 pull-right">
                    <div class="column">
                        <aside id="block-region-footer-right" class="block-region" data-blockregion="footer-right"
                            data-droptarget="1"></aside>
                    </div>
                </div>
            </div>
            <div class="footerlinks row-fluid">
                <hr />
                <span class="helplink"></span>
            </div>
            <div class="footerperformance row-fluid">
            </div>
            <div class="footercredit row-fluid">
                The Essential theme is developed, enhanced and maintained by <a href="//about.me/gjbarnard"
                    target="_blank">Gareth J Barnard</a>
            </div>
        </div>
    </footer>
    <a href="#top" class="back-to-top"><i class="fa fa-angle-up "></i></a>
    <!--js file commented and included in blocks/events instead of adding in theme footer-->
    <!--<script src="https://cdn.rawgit.com/vast-engineering/jquery-popup-overlay/1.7.10/jquery.popupoverlay.js"></script>-->
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/custom_zoom.js"></script>
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/select2.min.js"></script>
    <link href="https://mydy.dypatil.edu/rait/theme/essential/style/select2.min.css" rel="stylesheet" />

    <script type="text/javascript">
        jQuery(document).ready(function () {
            $('#id_cobaltcourseid').select2();
            $('#id_onlinecourseid').select2();
            jQuery('#essentialnavbar').affix({offset: {top: $('#page-header').height()}});$('#page').fitVids();        });
    </script>
    <script type="text/javascript">
        //<![CDATA[
var require = {
    baseUrl : 'https://mydy.dypatil.edu/rait/lib/requirejs.php/1709815567/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,

    paths: {
        jquery: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/jquery-1.11.2.min',
        jqueryui: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/ui-1.11.4/jquery-ui.min',
        jqueryprivate: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/require.min.js"></script>
    <script type="text/javascript">
        //<![CDATA[
require(['core/first'], function() {
;
require(["core/log"], function(amd) { amd.setConfig({"level":"warn"}); });
});
//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/ratings.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/facebook.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/twitter.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/footer">
    </script>
    <script type="text/javascript">
        //<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","viewallcourses":"View all courses","morehelp":"More help","loadinghelp":"Loading...","cancel":"Cancel","yes":"Yes","confirm":"Confirm","no":"No","areyousure":"Are you sure?","closebuttontitle":"Close","unknownerror":"Unknown error"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source","select":"Select"},"block":{"addtodock":"Move this to the dock","undockitem":"Undock this item","dockblock":"Dock {$a} block","undockblock":"Undock {$a} block","undockall":"Undock all","hidedockpanel":"Hide the dock panel","hidepanel":"Hide panel"},"langconfig":{"thisdirectionvertical":"btt"},"admin":{"confirmation":"Confirmation"}};
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
var navtreeexpansions4 = [{"id":"expandable_branch_30_168055","key":"168055","type":30},{"id":"expandable_branch_30_168117","key":"168117","type":30},{"id":"expandable_branch_30_168118","key":"168118","type":30},{"id":"expandable_branch_30_168119","key":"168119","type":30},{"id":"expandable_branch_30_168120","key":"168120","type":30},{"id":"expandable_branch_30_168121","key":"168121","type":30},{"id":"expandable_branch_30_168122","key":"168122","type":30},{"id":"expandable_branch_30_168123","key":"168123","type":30},{"id":"expandable_branch_30_168124","key":"168124","type":30},{"id":"expandable_branch_30_168125","key":"168125","type":30},{"id":"expandable_branch_30_168126","key":"168126","type":30},{"id":"expandable_branch_30_168477","key":"168477","type":30},{"id":"expandable_branch_30_168478","key":"168478","type":30},{"id":"expandable_branch_0_mycourses","key":"mycourses","type":0}];
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
YUI().use('node', function(Y) {
M.util.load_flowplayer();
setTimeout("fix_column_widths()", 20);
Y.use("moodle-core-dock-loader",function() {M.core.dock.loader.initLoader();
});
 M.util.js_pending('random663baf2df164d1'); Y.on('domready', function() { M.util.init_maximised_embed(Y, "questionpaperobject");  M.util.js_complete('random663baf2df164d1'); });
Y.use("moodle-theme_essential-zoom",function() {M.theme_essential.zoom.init();
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"19","instance":"19","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"4","instance":"4","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"5","instance":"5","candock":true});
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"31230","instance":"31230","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"en"});
});
M.util.help_popups.setup(Y);
Y.use("moodle-core-popuphelp",function() {M.core.init_popuphelp();
});
M.util.init_block_hider(Y, {"id":"inst19","title":"My tasks","preference":"block19hidden","tooltipVisible":"Hide My tasks block","tooltipHidden":"Show My tasks block"});
M.util.init_block_hider(Y, {"id":"inst5","title":"Administration","preference":"block5hidden","tooltipVisible":"Hide Administration block","tooltipHidden":"Show Administration block"});
M.util.init_block_hider(Y, {"id":"inst31230","title":"Previous semester classes","preference":"block31230hidden","tooltipVisible":"Hide Previous semester classes block","tooltipHidden":"Show Previous semester classes block"});
 M.util.js_pending('random663baf2df164d6'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random663baf2df164d6'); });

});
//]]>
    </script>
</body>

</html>
"""

response6 = """
<!DOCTYPE html>
<html dir="ltr" lang="en" xml:lang="en" class="no-js">

<head>
    <title>CAC403-22-A-AIML: 4</title>
    <link rel="shortcut icon" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/favicon" />
    <link rel="stylesheet"
        href="//mydy.dypatil.edu/rait/pluginfile.php/1/theme_essential/style/1709815567/essential.css">

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="keywords" content="moodle, CAC403-22-A-AIML: 4" />
    <script type="text/javascript">
        //<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/mydy.dypatil.edu\/rait","sesskey":"c5KroZlWWb","loadingicon":"https:\/\/mydy.dypatil.edu\/rait\/theme\/image.php\/essential\/core\/1709815567\/i\/loading_small","themerev":"1709815567","slasharguments":1,"theme":"essential","jsrev":"1709815567","admin":"admin","svgicons":true};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''};if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else me.path=component+'/'+component+'.'+me.type};
YUI_config = {"debug":false,"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?m\/1709815567\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"m\/1709815567\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-checknet":{"requires":["base-base","moodle-core-notification-alert","io-base"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-dock":{"requires":["base","node","event-custom","event-mouseenter","event-resize","escape","moodle-core-dock-loader"]},"moodle-core-dock-loader":{"requires":["escape"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-formautosubmit":{"requires":["base","event-key"]},"moodle-core-formchangechecker":{"requires":["base","event-focus"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core_availability-form":{"requires":["base","node","event","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-calendar-info":{"requires":["base","node","event-mouseenter","event-key","overlay","moodle-calendar-info-skin"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-modchooser":{"requires":["moodle-core-chooserdialogue","moodle-course-coursebase"]},"moodle-course-toolboxes":{"requires":["node","base","event-key","node","io","moodle-course-coursebase","moodle-course-util"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-passwordunmask":{"requires":["node","base"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-showadvanced":{"requires":["node","base","selector-css3"]},"moodle-core_message-messenger":{"requires":["escape","handlebars","io-base","moodle-core-notification-ajaxexception","moodle-core-notification-alert","moodle-core-notification-dialogue","moodle-core-notification-exception"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-qbankmanager":{"requires":["node","selector-css3"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_cohort-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_customcert-rearrange":{"requires":["dd-delegate","dd-drag"]},"moodle-mod_forum-subscriptiontoggle":{"requires":["base-base","io-base"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-quizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-core-notification-dialogue"]},"moodle-mod_quiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_navigation-navigation":{"requires":["base","io-base","node","event-synthetic","event-delegate","json-parse"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-format_grid-gridkeys":{"requires":["event-nav-keys"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_html-button":{"requires":["moodle-editor_atto-plugin","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1709815567\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.mathjax.org\/mathjax\/2.5-latest\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js&amp;rollup/1709815567/mcore-min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/jquery-1.11.2.min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/ui-1.11.4/jquery-ui.min.js">
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/bootstrap_2_3_2_min.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/jBreadCrumb_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/fitvids_1_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/anti_gravity_1_1.js"></script>
    <script id="firstthemesheet" type="text/css">
        /** Required in order to fix style inclusion problems in IE with YUI **/
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/styles.php/essential/1709815567/all" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/jquery-ui.css" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/style.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/javascript-static.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/head">
    </script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google web fonts -->
    <!--<link href='http://fonts.googleapis.com/css?family=Domine' rel='stylesheet' type='text/css'>-->
    <!-- iOS Homescreen Icons -->

    <link rel="apple-touch-icon-precomposed" sizes="57x57"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone_retina" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad_retina" />
    <!-- Start Analytics -->
    <!-- End Analytics -->

    <!--include custom fonts-->
    <style>
        @font-face {
            font-family: "Minion Pro Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/Minion-Pro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Light";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Light.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Semibold";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Semibold.ttf');
        }
    </style>

    <script type="text/javascript">
        $(document).ready(function() {
	  	//var $pwidth = $(window).width();
			//var $loggedin = $('body').hasClass('loggedin');

			/*if($pwidth >= 768){
				$('.offcanvas, #content-container').addClass('active');
			}*/

		  $('[data-toggle=offcanvas]').click(function() {

		  var $pwidth = $(window).width();
			$('.offcanvas').toggleClass('active');
			$('#content-container').toggleClass('active');

			//do this when in nmobile view
			var $main = $('main').hasClass('active');
			if($pwidth <= 480 ){

				if( $main == true){
					$('body, html').addClass('noscroll');
				}else{
					$('body, html').removeClass('noscroll');
				}
			}

			//do this when in tab/desktop view
			if($pwidth >= 481 ){

				//var $main = $('main').hasClass('active');

				if( $main == false){
					$('body, html').removeClass('noscroll');
				}
			}

		  });
        });
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS starts here -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-62316529-3"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag("js", new Date());
            gtag("config", "UA-62316529-3");
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS ends here -->
</head>

<body id="page-mod-dyquestion-view"
    class="format-topcoll  path-mod path-mod-dyquestion dir-ltr lang-en yui-skin-sam yui3-skin-sam mydy-dypatil-edu--rait pagelayout-incourse course-5921 context-730439 cmid-610185 category-879 desktopdevice pagewidthnormal categoryicons zoomin two-column  has-region-side-pre used-region-side-pre has-region-footer-left empty-region-footer-left has-region-footer-middle empty-region-footer-middle has-region-footer-right empty-region-footer-right side-pre-only">

    <div class="skiplinks"><a class="skip" href="#maincontent">Skip to main content</a></div>
    <script type="text/javascript">
        //<![CDATA[
document.body.className += ' jsenabled';
//]]>
    </script>


    <header role="banner">
        <div id="page-header" class="clearfix oldnavbar">
            <div class="container-fluid">
                <div class="row-fluid">
                    <!-- HEADER: LOGO AREA -->
                    <div class="ecol12 pull-left">
                        <a class="logo" href="//mydy.dypatil.edu/rait" title="Home"></a>
                        <nav role="navigation">
                            <div class="topnavbar navbar oldnavbar moodle-has-zindex">
                                <div class="container-fluid navbar-inner">
                                    <div class="row-fluid">
                                        <div class="pull-right">
                                            <div class="usermenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a class="dropdown-toggle"
                                                            data-toggle="dropdown"
                                                            href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu pull-right">
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a>
                                                            </li>
                                                            <li class="dropdown-submenu preferences"><a
                                                                    class="dropdown-toggle" data-toggle="dropdown"
                                                                    href="#"><em><i class="fa fa-cog"></i>Preferences</em></a>
                                                                <ul class="dropdown-menu">
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a>
                                                                    </li>
                                                                </ul>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a>
                                                            </li>
                                                            <li><a target=""
                                                                    href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="messagemenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a
                                                            href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations"
                                                            class="dropdown-toggle" data-toggle="dropdown"
                                                            title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu">
                                                            <li><a title="You have submitted your assignment submission for Vlab - ER modeling"
                                                                    href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950">
                                                                    <div class="notification read">
                                                                        <i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span>
                                                                    </div>
                                                                </a>
                                                        </ul>
                                                </ul>
                                            </div>
                                            <div class="messagemenu messagemenu_video">
                                                <ul class="nav">
                                                    <li><a class="videotutorial"
                                                            href="https://mydy.dypatil.edu/rait/mod/page/view.php?id=101">Training
                                                            Video</a></li>
                                                </ul>
                                            </div>
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <div class="gotobottommenu">
                                                <ul class="nav">
                                                    <li><a title="Go to the bottom of the page"
                                                            href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </nav>
                    </div>


                </div>
            </div>
        </div>
        <nav role="navigation">
            <div id='essentialnavbar' class="navbar oldnavbar moodle-has-zindex">
                <div class="container-fluid navbar-inner">
                    <div class="row-fluid">
                        <div class="custommenus pull-left">
                            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </a>
                            <!--<div class="pull-right">-->
                            <!--    <div class="usermenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="gotobottommenu">-->
                            <!--        <ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>-->
                            <!--    </div>-->
                            <!--</div>-->
                            <div class="nav-collapse collapse pull-left">
                                <div id="custom_menu_language">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_courses">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_activitystream">
                                </div>
                                <ul class="nav pull-left">
                                    <li class="hbl"><a href="#" class="moodlezoom"><i class="fa fa-outdent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                    <li class="sbl"><a href="#" class="moodlezoom"><i class="fa fa-indent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                </ul>

                                <!--******************code added by anil-started here*******************-->
                                <div id="custom_menu_topmenu">
                                    <!--*********code added by anil*************-->
                                    <ul class="nav">
                                        <li><a href="https://mydy.dypatil.edu/rait/" class="navbarlinks">Home</a></li>
                                        <li><a href="http://m.p-y.tm/PUPRTT" class="navbarlinks" target="_blank">Fee
                                                Payment</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php"
                                                class="navbarlinks">Exams</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/dypmarket/index.php"
                                                id="marketplace">Market Place</a></li>
                                    </ul>
                                    <!--******************code added by anil-ended here*******************-->
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <div id="page" class="container-fluid">
        <div id="page-navbar" class="clearfix row-fluid">
            <div class="breadcrumb-nav pull-left">
                <ul class="breadcrumb style2">
                    <li style="z-index:99;"><a href="https://mydy.dypatil.edu/rait/my/">Dashboard</a></li>
                    <li style="z-index:98;"><a title="Operating System"
                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921">CAC403-22-A-AIML</a></li>
                    <li style="z-index:97;"><span tabindex="0">IA1  Question bank</span></li>
                    <li style="z-index:96;"><a title="Question Bank"
                            href="https://mydy.dypatil.edu/rait/mod/dyquestion/view.php?id=610185">4</a></li>
                </ul>
            </div>
            <nav class="breadcrumb-button pull-right"></nav>
        </div>
        <section role="main-content">
            <!-- Start Main Regions -->
            <div id="page-content" class="row-fluid">
                <div id="region-bs-main-and-pre" class="span12">
                    <div class="row-fluid">
                        <section id="region-main" class="span9 pull-right">
                            <h1 class="coursetitle">Operating System</h1>
                            <div class="bor"></div>
                            <div role="main"><span id="maincontent"></span>
                                <h2>4</h2>
                                <div class="dyquestioncontent dyquestionpdf">
                                    <object id="dyquestionobject" data="https://mydy.dypatil.edu/rait/pluginfile.php/730439/mod_dyquestion/content/1/OS%20Question%20Bank-Week%204.pdf" type="application/pdf" width="800" height="600">
    <param name="src" value="https://mydy.dypatil.edu/rait/pluginfile.php/730439/mod_dyquestion/content/1/OS%20Question%20Bank-Week%204.pdf" />
    Click <a href="https://mydy.dypatil.edu/rait/pluginfile.php/730439/mod_dyquestion/content/1/OS%20Question%20Bank-Week%204.pdf" >OS Question Bank-Week 4.pdf</a> link to view the file.
  </object>
                                </div>
                                <div id="fb-root"></div>
                                <div id="myratings"></div>
                                <div id="dyquestion_pages">
                                    <div class="like_unlike">
                                        <div id="contents_49611" style="float: left;">
                                            <div id="label_like_49611" style="float: left; padding: 0 8px 0 0;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;dyquestion&quot;, 610185, 49611, 5921, 0)" />
                                            </div>
                                            <span  id="count_likearea" class="count_likearea_49611"><a id="anchorclass_49611" href="javascript:void(0)" onClick="fnViewAllLikes(49611)">0</a></span>
                                            <div class="courselike" id="like_list_49611" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon49611"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="like_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Likes</b></span>
                                                <div class="like_49611"></div>
                                            </div>
                                            <div id="label_unlike_49611"
                                                style="float: left; padding: 0 8px 0 10px; margin-top:5px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Dislike" id="unlikeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;dyquestion&quot;, 610185, 49611, 5921, 1)" />
                                            </div>
                                            <span id="count_unlikearea"  class="count_unlikearea_49611"><a id="anchorclass_49611" href="javascript:void(0)" onClick="fnViewAllunLikes(49611)">0</a></span>
                                            <div class="courseunlike" id="unlike_list_49611" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon49611"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="unlike_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Unlikes</b></span>
                                                <div class="unlike_49611"></div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="radiostars">
                                        <div class="overall_ratings_49611" style="float: left; cursor: pointer;"><img title='0 out of 5' src='https://mydy.dypatil.edu/rait/local/ratings/pix/star0.png'  onclick='fnViewAllRatings(5921, 610185, 49611, "dyquestion", "https://mydy.dypatil.edu/rait", "4")'/>
                                        </div>
                                        <div class="overall_users">(<font class='totalcount_49611'>0</font> users)</div>
                                    </div>
                                    <div class="mycomment"><a id="anchorclass_49611" href="javascript:void(0)"
                                            onClick="fnViewAllComments(49611)"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/comment.png" title="Comment" id="custom_icons" /></a>&nbsp;(
                                        <font class="commentcount_49611">0</font>)<div class="coursecomment"
                                            id="comment_list_49611" style="display: none;">
                                            <div style="float: right; cursor: pointer;" class="closeicon49611"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="comment_closeicon" />
                                            </div>
                                            <textarea name="commentarea" id="mycomment_49611" rows="2" cols="50"></textarea><a
                                                class="commentclick_49611" href="javascript:void(0)"
                                                onClick="fnComment(5921, 610185, 49611, &quot;dyquestion&quot;, &quot;https://mydy.dypatil.edu/rait&quot;)"
                                                style="font-size: 12px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/add-comment.gif" /></a>
                                            <div class="comment_49611"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <aside id="block-region-side-pre" class="span3 desktop-first-column block-region"
                            data-blockregion="side-pre" data-droptarget="1"><a href="#sb-1" class="skip-block">Skip My
                                tasks</a>
                            <div id="inst19" class="block_universitystructure  block" role="complementary"
                                data-block="universitystructure" data-instanceid="19"
                                aria-labelledby="instance-19-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-19-header">My tasks</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Learnings</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/timetable/calendarview.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">TimeTable Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/myacademics/transcript.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Transcript</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/academiccalendar"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Academic Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/feemanagement/studentfeedetails.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Fee Details</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        <li class="type_category depth_3 contains_branch">
                                            <p class="tree_item branch active_tree_node">
                                                <span class="usdimmed_text" >Examination</span>
                                            <ul>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php">Scheduled
                                                            Exams</a></p>
                                                </li>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/studentresults.php">Student
                                                            Examsresults </a></p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_3 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Profile</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/profile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">View Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Edit Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/change_password.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Change Password</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-1" class="skip-block-to"></span><a href="#sb-3" class="skip-block">Skip
                                Administration</a>
                            <div id="inst5" class="block_settings  block" role="navigation" data-block="settings"
                                data-instanceid="5" aria-labelledby="instance-5-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-5-header">Administration</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <div id="settingsnav" class="box block_tree_box">
                                        <ul class="block_tree list">
                                            <li class="type_course collapsed contains_branch" aria-expanded="false">
                                                <p class="tree_item branch root_node">
                                                    <span tabindex="0">Course administration</span></p>
                                                <ul>
                                                    <li class="type_setting collapsed item_with_icon">
                                                        <p class="tree_item leaf"><a
                                                                href="https://mydy.dypatil.edu/rait/grade/report/index.php?id=5921"><i class="fa fa-table icon" title=""><img alt="" class="smallicon navicon" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/grades" /></i>Grades</a>
                                                        </p>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div><span id="sb-3" class="skip-block-to"></span><a href="#sb-5" class="skip-block">Skip
                                Previous semester classes</a>
                            <div id="inst31230" class="block_stu_previousclasses  block" role="complementary"
                                data-block="stu_previousclasses" data-instanceid="31230"
                                aria-labelledby="instance-31230-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-31230-header">Previous semester classes</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasiconactive_tree_node">
                                                <span class="usdimmed_text" >Semester I</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4642"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics I</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4643"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Structered Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4644"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Electronics Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4645"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Physics</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4646"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">English For Engineers</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester II</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5067"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics-II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5068"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Chemistry II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5069"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Data Structures</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5071"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Digital Logic Design</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5072"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Environmental Studies</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5070"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Communication Engineering</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester III</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5197"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Database Management System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5198"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Design and Analysis of Algorithms</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5199"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Object Oriented Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5200"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Computer Organization & Architecture</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5201"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Statistical Methods</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester IV</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5919"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Artificial Intelligence</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5920"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Software Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Operating System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Programming with Python</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5923"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Formal Language Automata Language</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-5" class="skip-block-to"></span>
                        </aside>
                    </div>
                </div>
            </div>
            <!-- End Main Regions -->
        </section>
    </div>

    <footer role="contentinfo" id="page-footer">
        <div class="container-fluid">
            <div class="row-fluid footerblocks">
                <div class="span8 pull-left footersite-text">
                    <p>
                    <h4>'Education is not the learning of many facts </h4>
                    </p>
                    <p>
                    <h4>but the training of the mind to think.' - Albert Einstein</h4>
                    </p>
                </div>
                <div class="span4 pull-right footersite-icons">
                </div>
            </div>
            <div class="row-fluid footerblocks">
                <div class="span4 pull-left">
                    <div class="column">
                        <aside id="block-region-footer-left" class="block-region" data-blockregion="footer-left"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 center">
                    <div class="column">
                        <aside id="block-region-footer-middle" class="block-region" data-blockregion="footer-middle"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 pull-right">
                    <div class="column">
                        <aside id="block-region-footer-right" class="block-region" data-blockregion="footer-right"
                            data-droptarget="1"></aside>
                    </div>
                </div>
            </div>
            <div class="footerlinks row-fluid">
                <hr />
                <span class="helplink"></span>
            </div>
            <div class="footerperformance row-fluid">
            </div>
            <div class="footercredit row-fluid">
                The Essential theme is developed, enhanced and maintained by <a href="//about.me/gjbarnard"
                    target="_blank">Gareth J Barnard</a>
            </div>
        </div>
    </footer>
    <a href="#top" class="back-to-top"><i class="fa fa-angle-up "></i></a>
    <!--js file commented and included in blocks/events instead of adding in theme footer-->
    <!--<script src="https://cdn.rawgit.com/vast-engineering/jquery-popup-overlay/1.7.10/jquery.popupoverlay.js"></script>-->
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/custom_zoom.js"></script>
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/select2.min.js"></script>
    <link href="https://mydy.dypatil.edu/rait/theme/essential/style/select2.min.css" rel="stylesheet" />

    <script type="text/javascript">
        jQuery(document).ready(function () {
            $('#id_cobaltcourseid').select2();
            $('#id_onlinecourseid').select2();
            jQuery('#essentialnavbar').affix({offset: {top: $('#page-header').height()}});$('#page').fitVids();        });
    </script>
    <script type="text/javascript">
        //<![CDATA[
var require = {
    baseUrl : 'https://mydy.dypatil.edu/rait/lib/requirejs.php/1709815567/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,

    paths: {
        jquery: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/jquery-1.11.2.min',
        jqueryui: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/ui-1.11.4/jquery-ui.min',
        jqueryprivate: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/require.min.js"></script>
    <script type="text/javascript">
        //<![CDATA[
require(['core/first'], function() {
;
require(["core/log"], function(amd) { amd.setConfig({"level":"warn"}); });
});
//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/ratings.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/facebook.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/twitter.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/footer">
    </script>
    <script type="text/javascript">
        //<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","viewallcourses":"View all courses","morehelp":"More help","loadinghelp":"Loading...","cancel":"Cancel","yes":"Yes","confirm":"Confirm","no":"No","areyousure":"Are you sure?","closebuttontitle":"Close","unknownerror":"Unknown error"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source","select":"Select"},"block":{"addtodock":"Move this to the dock","undockitem":"Undock this item","dockblock":"Dock {$a} block","undockblock":"Undock {$a} block","undockall":"Undock all","hidedockpanel":"Hide the dock panel","hidepanel":"Hide panel"},"langconfig":{"thisdirectionvertical":"btt"},"admin":{"confirmation":"Confirmation"}};
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
var navtreeexpansions4 = [{"id":"expandable_branch_30_168055","key":"168055","type":30},{"id":"expandable_branch_30_168117","key":"168117","type":30},{"id":"expandable_branch_30_168118","key":"168118","type":30},{"id":"expandable_branch_30_168119","key":"168119","type":30},{"id":"expandable_branch_30_168120","key":"168120","type":30},{"id":"expandable_branch_30_168121","key":"168121","type":30},{"id":"expandable_branch_30_168122","key":"168122","type":30},{"id":"expandable_branch_30_168123","key":"168123","type":30},{"id":"expandable_branch_30_168124","key":"168124","type":30},{"id":"expandable_branch_30_168125","key":"168125","type":30},{"id":"expandable_branch_30_168126","key":"168126","type":30},{"id":"expandable_branch_30_168477","key":"168477","type":30},{"id":"expandable_branch_30_168478","key":"168478","type":30},{"id":"expandable_branch_0_mycourses","key":"mycourses","type":0}];
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
YUI().use('node', function(Y) {
M.util.load_flowplayer();
setTimeout("fix_column_widths()", 20);
Y.use("moodle-core-dock-loader",function() {M.core.dock.loader.initLoader();
});
 M.util.js_pending('random663baf81468bb1'); Y.on('domready', function() { M.util.init_maximised_embed(Y, "dyquestionobject");  M.util.js_complete('random663baf81468bb1'); });
Y.use("moodle-theme_essential-zoom",function() {M.theme_essential.zoom.init();
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"19","instance":"19","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"4","instance":"4","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"5","instance":"5","candock":true});
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"31230","instance":"31230","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"en"});
});
M.util.help_popups.setup(Y);
Y.use("moodle-core-popuphelp",function() {M.core.init_popuphelp();
});
M.util.init_block_hider(Y, {"id":"inst19","title":"My tasks","preference":"block19hidden","tooltipVisible":"Hide My tasks block","tooltipHidden":"Show My tasks block"});
M.util.init_block_hider(Y, {"id":"inst5","title":"Administration","preference":"block5hidden","tooltipVisible":"Hide Administration block","tooltipHidden":"Show Administration block"});
M.util.init_block_hider(Y, {"id":"inst31230","title":"Previous semester classes","preference":"block31230hidden","tooltipVisible":"Hide Previous semester classes block","tooltipHidden":"Show Previous semester classes block"});
 M.util.js_pending('random663baf81468bb6'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random663baf81468bb6'); });

});
//]]>
    </script>
</body>

</html>
"""

response7 = """
<!DOCTYPE html>
<html dir="ltr" lang="en" xml:lang="en" class="no-js">

<head>
    <title>CAC403-22-A-AIML: Classical IPC Problem </title>
    <link rel="shortcut icon" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/favicon" />
    <link rel="stylesheet"
        href="//mydy.dypatil.edu/rait/pluginfile.php/1/theme_essential/style/1709815567/essential.css">

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="keywords" content="moodle, CAC403-22-A-AIML: Classical IPC Problem " />
    <script type="text/javascript">
        //<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/mydy.dypatil.edu\/rait","sesskey":"c5KroZlWWb","loadingicon":"https:\/\/mydy.dypatil.edu\/rait\/theme\/image.php\/essential\/core\/1709815567\/i\/loading_small","themerev":"1709815567","slasharguments":1,"theme":"essential","jsrev":"1709815567","admin":"admin","svgicons":true};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''};if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else me.path=component+'/'+component+'.'+me.type};
YUI_config = {"debug":false,"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?m\/1709815567\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"m\/1709815567\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-checknet":{"requires":["base-base","moodle-core-notification-alert","io-base"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-dock":{"requires":["base","node","event-custom","event-mouseenter","event-resize","escape","moodle-core-dock-loader"]},"moodle-core-dock-loader":{"requires":["escape"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-formautosubmit":{"requires":["base","event-key"]},"moodle-core-formchangechecker":{"requires":["base","event-focus"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core_availability-form":{"requires":["base","node","event","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-calendar-info":{"requires":["base","node","event-mouseenter","event-key","overlay","moodle-calendar-info-skin"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-modchooser":{"requires":["moodle-core-chooserdialogue","moodle-course-coursebase"]},"moodle-course-toolboxes":{"requires":["node","base","event-key","node","io","moodle-course-coursebase","moodle-course-util"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-passwordunmask":{"requires":["node","base"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-showadvanced":{"requires":["node","base","selector-css3"]},"moodle-core_message-messenger":{"requires":["escape","handlebars","io-base","moodle-core-notification-ajaxexception","moodle-core-notification-alert","moodle-core-notification-dialogue","moodle-core-notification-exception"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-qbankmanager":{"requires":["node","selector-css3"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_cohort-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_customcert-rearrange":{"requires":["dd-delegate","dd-drag"]},"moodle-mod_forum-subscriptiontoggle":{"requires":["base-base","io-base"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-quizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-core-notification-dialogue"]},"moodle-mod_quiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_navigation-navigation":{"requires":["base","io-base","node","event-synthetic","event-delegate","json-parse"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-format_grid-gridkeys":{"requires":["event-nav-keys"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_html-button":{"requires":["moodle-editor_atto-plugin","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1709815567\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.mathjax.org\/mathjax\/2.5-latest\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js&amp;rollup/1709815567/mcore-min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/jquery-1.11.2.min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/ui-1.11.4/jquery-ui.min.js">
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/bootstrap_2_3_2_min.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/jBreadCrumb_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/fitvids_1_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/anti_gravity_1_1.js"></script>
    <script id="firstthemesheet" type="text/css">
        /** Required in order to fix style inclusion problems in IE with YUI **/
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/styles.php/essential/1709815567/all" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/jquery-ui.css" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/style.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/javascript-static.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/head">
    </script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google web fonts -->
    <!--<link href='http://fonts.googleapis.com/css?family=Domine' rel='stylesheet' type='text/css'>-->
    <!-- iOS Homescreen Icons -->

    <link rel="apple-touch-icon-precomposed" sizes="57x57"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone_retina" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad_retina" />
    <!-- Start Analytics -->
    <!-- End Analytics -->

    <!--include custom fonts-->
    <style>
        @font-face {
            font-family: "Minion Pro Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/Minion-Pro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Light";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Light.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Semibold";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Semibold.ttf');
        }
    </style>

    <script type="text/javascript">
        $(document).ready(function() {
	  	//var $pwidth = $(window).width();
			//var $loggedin = $('body').hasClass('loggedin');

			/*if($pwidth >= 768){
				$('.offcanvas, #content-container').addClass('active');
			}*/

		  $('[data-toggle=offcanvas]').click(function() {

		  var $pwidth = $(window).width();
			$('.offcanvas').toggleClass('active');
			$('#content-container').toggleClass('active');

			//do this when in nmobile view
			var $main = $('main').hasClass('active');
			if($pwidth <= 480 ){

				if( $main == true){
					$('body, html').addClass('noscroll');
				}else{
					$('body, html').removeClass('noscroll');
				}
			}

			//do this when in tab/desktop view
			if($pwidth >= 481 ){

				//var $main = $('main').hasClass('active');

				if( $main == false){
					$('body, html').removeClass('noscroll');
				}
			}

		  });
        });
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS starts here -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-62316529-3"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag("js", new Date());
            gtag("config", "UA-62316529-3");
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS ends here -->
</head>

<body id="page-mod-presentation-view"
    class="format-topcoll  path-mod path-mod-presentation dir-ltr lang-en yui-skin-sam yui3-skin-sam mydy-dypatil-edu--rait pagelayout-incourse course-5921 context-726991 cmid-606809 category-879 desktopdevice pagewidthnormal categoryicons zoomin two-column  has-region-side-pre used-region-side-pre has-region-footer-left empty-region-footer-left has-region-footer-middle empty-region-footer-middle has-region-footer-right empty-region-footer-right side-pre-only">

    <div class="skiplinks"><a class="skip" href="#maincontent">Skip to main content</a></div>
    <script type="text/javascript">
        //<![CDATA[
document.body.className += ' jsenabled';
//]]>
    </script>


    <header role="banner">
        <div id="page-header" class="clearfix oldnavbar">
            <div class="container-fluid">
                <div class="row-fluid">
                    <!-- HEADER: LOGO AREA -->
                    <div class="ecol12 pull-left">
                        <a class="logo" href="//mydy.dypatil.edu/rait" title="Home"></a>
                        <nav role="navigation">
                            <div class="topnavbar navbar oldnavbar moodle-has-zindex">
                                <div class="container-fluid navbar-inner">
                                    <div class="row-fluid">
                                        <div class="pull-right">
                                            <div class="usermenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a class="dropdown-toggle"
                                                            data-toggle="dropdown"
                                                            href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu pull-right">
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a>
                                                            </li>
                                                            <li class="dropdown-submenu preferences"><a
                                                                    class="dropdown-toggle" data-toggle="dropdown"
                                                                    href="#"><em><i class="fa fa-cog"></i>Preferences</em></a>
                                                                <ul class="dropdown-menu">
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a>
                                                                    </li>
                                                                </ul>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a>
                                                            </li>
                                                            <li><a target=""
                                                                    href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="messagemenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a
                                                            href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations"
                                                            class="dropdown-toggle" data-toggle="dropdown"
                                                            title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu">
                                                            <li><a title="You have submitted your assignment submission for Vlab - ER modeling"
                                                                    href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950">
                                                                    <div class="notification read">
                                                                        <i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span>
                                                                    </div>
                                                                </a>
                                                        </ul>
                                                </ul>
                                            </div>
                                            <div class="messagemenu messagemenu_video">
                                                <ul class="nav">
                                                    <li><a class="videotutorial"
                                                            href="https://mydy.dypatil.edu/rait/mod/page/view.php?id=101">Training
                                                            Video</a></li>
                                                </ul>
                                            </div>
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <div class="gotobottommenu">
                                                <ul class="nav">
                                                    <li><a title="Go to the bottom of the page"
                                                            href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </nav>
                    </div>


                </div>
            </div>
        </div>
        <nav role="navigation">
            <div id='essentialnavbar' class="navbar oldnavbar moodle-has-zindex">
                <div class="container-fluid navbar-inner">
                    <div class="row-fluid">
                        <div class="custommenus pull-left">
                            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </a>
                            <!--<div class="pull-right">-->
                            <!--    <div class="usermenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="gotobottommenu">-->
                            <!--        <ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>-->
                            <!--    </div>-->
                            <!--</div>-->
                            <div class="nav-collapse collapse pull-left">
                                <div id="custom_menu_language">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_courses">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_activitystream">
                                </div>
                                <ul class="nav pull-left">
                                    <li class="hbl"><a href="#" class="moodlezoom"><i class="fa fa-outdent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                    <li class="sbl"><a href="#" class="moodlezoom"><i class="fa fa-indent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                </ul>

                                <!--******************code added by anil-started here*******************-->
                                <div id="custom_menu_topmenu">
                                    <!--*********code added by anil*************-->
                                    <ul class="nav">
                                        <li><a href="https://mydy.dypatil.edu/rait/" class="navbarlinks">Home</a></li>
                                        <li><a href="http://m.p-y.tm/PUPRTT" class="navbarlinks" target="_blank">Fee
                                                Payment</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php"
                                                class="navbarlinks">Exams</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/dypmarket/index.php"
                                                id="marketplace">Market Place</a></li>
                                    </ul>
                                    <!--******************code added by anil-ended here*******************-->
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <div id="page" class="container-fluid">
        <div id="page-navbar" class="clearfix row-fluid">
            <div class="breadcrumb-nav pull-left">
                <ul class="breadcrumb style2">
                    <li style="z-index:99;"><a href="https://mydy.dypatil.edu/rait/my/">Dashboard</a></li>
                    <li style="z-index:98;"><a title="Operating System"
                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921">CAC403-22-A-AIML</a></li>
                    <li style="z-index:97;"><span tabindex="0">Week 6</span></li>
                    <li style="z-index:96;"><a title="Presentation (Download)"
                            href="https://mydy.dypatil.edu/rait/mod/presentation/view.php?id=606809">Classical IPC
                            Problem </a></li>
                </ul>
            </div>
            <nav class="breadcrumb-button pull-right"></nav>
        </div>
        <section role="main-content">
            <!-- Start Main Regions -->
            <div id="page-content" class="row-fluid">
                <div id="region-bs-main-and-pre" class="span12">
                    <div class="row-fluid">
                        <section id="region-main" class="span9 pull-right">
                            <h1 class="coursetitle">Operating System</h1>
                            <div class="bor"></div>
                            <div role="main"><span id="maincontent"></span>
                                <h2>Classical IPC Problem </h2>
                                <div class="presentationcontent presentationgeneral">
                                    <iframe id="presentationobject"
                                        src="https://mydy.dypatil.edu/rait/pluginfile.php/726991/mod_presentation/content/1/DYPU-SE-OS-Sem%204_Week%206%20L16-Lec18-Classical%20IPC%20Problem.pptx">
                                        Click <a
                                            href="https://mydy.dypatil.edu/rait/pluginfile.php/726991/mod_presentation/content/1/DYPU-SE-OS-Sem%204_Week%206%20L16-Lec18-Classical%20IPC%20Problem.pptx">DYPU-SE-OS-Sem
                                            4_Week 6 L16-Lec18-Classical IPC Problem.pptx</a> link to view the file.
                                    </iframe>
                                </div>
                                <div id="fb-root"></div>
                                <div id="myratings"></div>
                                <div id="presentation_pages">
                                    <div class="like_unlike">
                                        <div id="contents_28392" style="float: left;">
                                            <div id="label_like_28392" style="float: left; padding: 0 8px 0 0;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;presentation&quot;, 606809, 28392, 5921, 0)" />
                                            </div>
                                            <span  id="count_likearea" class="count_likearea_28392"><a id="anchorclass_28392" href="javascript:void(0)" onClick="fnViewAllLikes(28392)">0</a></span>
                                            <div class="courselike" id="like_list_28392" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon28392"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="like_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Likes</b></span>
                                                <div class="like_28392"></div>
                                            </div>
                                            <div id="label_unlike_28392"
                                                style="float: left; padding: 0 8px 0 10px; margin-top:5px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Dislike" id="unlikeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;presentation&quot;, 606809, 28392, 5921, 1)" />
                                            </div>
                                            <span id="count_unlikearea"  class="count_unlikearea_28392"><a id="anchorclass_28392" href="javascript:void(0)" onClick="fnViewAllunLikes(28392)">0</a></span>
                                            <div class="courseunlike" id="unlike_list_28392" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon28392"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="unlike_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Unlikes</b></span>
                                                <div class="unlike_28392"></div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="radiostars">
                                        <div class="overall_ratings_28392" style="float: left; cursor: pointer;"><img title='0 out of 5' src='https://mydy.dypatil.edu/rait/local/ratings/pix/star0.png'  onclick='fnViewAllRatings(5921, 606809, 28392, "presentation", "https://mydy.dypatil.edu/rait", "Classical IPC Problem ")'/>
                                        </div>
                                        <div class="overall_users">(<font class='totalcount_28392'>0</font> users)</div>
                                    </div>
                                    <div class="mycomment"><a id="anchorclass_28392" href="javascript:void(0)"
                                            onClick="fnViewAllComments(28392)"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/comment.png" title="Comment" id="custom_icons" /></a>&nbsp;(
                                        <font class="commentcount_28392">0</font>)<div class="coursecomment"
                                            id="comment_list_28392" style="display: none;">
                                            <div style="float: right; cursor: pointer;" class="closeicon28392"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="comment_closeicon" />
                                            </div>
                                            <textarea name="commentarea" id="mycomment_28392" rows="2" cols="50"></textarea><a
                                                class="commentclick_28392" href="javascript:void(0)"
                                                onClick="fnComment(5921, 606809, 28392, &quot;presentation&quot;, &quot;https://mydy.dypatil.edu/rait&quot;)"
                                                style="font-size: 12px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/add-comment.gif" /></a>
                                            <div class="comment_28392"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <aside id="block-region-side-pre" class="span3 desktop-first-column block-region"
                            data-blockregion="side-pre" data-droptarget="1"><a href="#sb-1" class="skip-block">Skip My
                                tasks</a>
                            <div id="inst19" class="block_universitystructure  block" role="complementary"
                                data-block="universitystructure" data-instanceid="19"
                                aria-labelledby="instance-19-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-19-header">My tasks</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Learnings</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/timetable/calendarview.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">TimeTable Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/myacademics/transcript.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Transcript</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/academiccalendar"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Academic Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/feemanagement/studentfeedetails.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Fee Details</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        <li class="type_category depth_3 contains_branch">
                                            <p class="tree_item branch active_tree_node">
                                                <span class="usdimmed_text" >Examination</span>
                                            <ul>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php">Scheduled
                                                            Exams</a></p>
                                                </li>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/studentresults.php">Student
                                                            Examsresults </a></p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_3 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Profile</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/profile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">View Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Edit Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/change_password.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Change Password</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-1" class="skip-block-to"></span><a href="#sb-3" class="skip-block">Skip
                                Administration</a>
                            <div id="inst5" class="block_settings  block" role="navigation" data-block="settings"
                                data-instanceid="5" aria-labelledby="instance-5-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-5-header">Administration</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <div id="settingsnav" class="box block_tree_box">
                                        <ul class="block_tree list">
                                            <li class="type_course collapsed contains_branch" aria-expanded="false">
                                                <p class="tree_item branch root_node">
                                                    <span tabindex="0">Course administration</span></p>
                                                <ul>
                                                    <li class="type_setting collapsed item_with_icon">
                                                        <p class="tree_item leaf"><a
                                                                href="https://mydy.dypatil.edu/rait/grade/report/index.php?id=5921"><i class="fa fa-table icon" title=""><img alt="" class="smallicon navicon" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/grades" /></i>Grades</a>
                                                        </p>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div><span id="sb-3" class="skip-block-to"></span><a href="#sb-5" class="skip-block">Skip
                                Previous semester classes</a>
                            <div id="inst31230" class="block_stu_previousclasses  block" role="complementary"
                                data-block="stu_previousclasses" data-instanceid="31230"
                                aria-labelledby="instance-31230-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-31230-header">Previous semester classes</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasiconactive_tree_node">
                                                <span class="usdimmed_text" >Semester I</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4642"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics I</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4643"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Structered Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4644"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Electronics Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4645"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Physics</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4646"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">English For Engineers</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester II</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5067"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics-II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5068"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Chemistry II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5069"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Data Structures</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5071"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Digital Logic Design</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5072"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Environmental Studies</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5070"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Communication Engineering</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester III</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5197"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Database Management System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5198"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Design and Analysis of Algorithms</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5199"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Object Oriented Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5200"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Computer Organization & Architecture</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5201"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Statistical Methods</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester IV</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5919"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Artificial Intelligence</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5920"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Software Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Operating System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Programming with Python</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5923"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Formal Language Automata Language</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-5" class="skip-block-to"></span>
                        </aside>
                    </div>
                </div>
            </div>
            <!-- End Main Regions -->
        </section>
    </div>

    <footer role="contentinfo" id="page-footer">
        <div class="container-fluid">
            <div class="row-fluid footerblocks">
                <div class="span8 pull-left footersite-text">
                    <p>
                    <h4>'Education is not the learning of many facts </h4>
                    </p>
                    <p>
                    <h4>but the training of the mind to think.' - Albert Einstein</h4>
                    </p>
                </div>
                <div class="span4 pull-right footersite-icons">
                </div>
            </div>
            <div class="row-fluid footerblocks">
                <div class="span4 pull-left">
                    <div class="column">
                        <aside id="block-region-footer-left" class="block-region" data-blockregion="footer-left"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 center">
                    <div class="column">
                        <aside id="block-region-footer-middle" class="block-region" data-blockregion="footer-middle"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 pull-right">
                    <div class="column">
                        <aside id="block-region-footer-right" class="block-region" data-blockregion="footer-right"
                            data-droptarget="1"></aside>
                    </div>
                </div>
            </div>
            <div class="footerlinks row-fluid">
                <hr />
                <span class="helplink"></span>
            </div>
            <div class="footerperformance row-fluid">
            </div>
            <div class="footercredit row-fluid">
                The Essential theme is developed, enhanced and maintained by <a href="//about.me/gjbarnard"
                    target="_blank">Gareth J Barnard</a>
            </div>
        </div>
    </footer>
    <a href="#top" class="back-to-top"><i class="fa fa-angle-up "></i></a>
    <!--js file commented and included in blocks/events instead of adding in theme footer-->
    <!--<script src="https://cdn.rawgit.com/vast-engineering/jquery-popup-overlay/1.7.10/jquery.popupoverlay.js"></script>-->
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/custom_zoom.js"></script>
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/select2.min.js"></script>
    <link href="https://mydy.dypatil.edu/rait/theme/essential/style/select2.min.css" rel="stylesheet" />

    <script type="text/javascript">
        jQuery(document).ready(function () {
            $('#id_cobaltcourseid').select2();
            $('#id_onlinecourseid').select2();
            jQuery('#essentialnavbar').affix({offset: {top: $('#page-header').height()}});$('#page').fitVids();        });
    </script>
    <script type="text/javascript">
        //<![CDATA[
var require = {
    baseUrl : 'https://mydy.dypatil.edu/rait/lib/requirejs.php/1709815567/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,

    paths: {
        jquery: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/jquery-1.11.2.min',
        jqueryui: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/ui-1.11.4/jquery-ui.min',
        jqueryprivate: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/require.min.js"></script>
    <script type="text/javascript">
        //<![CDATA[
require(['core/first'], function() {
;
require(["core/log"], function(amd) { amd.setConfig({"level":"warn"}); });
});
//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/ratings.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/facebook.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/twitter.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/footer">
    </script>
    <script type="text/javascript">
        //<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","viewallcourses":"View all courses","morehelp":"More help","loadinghelp":"Loading...","cancel":"Cancel","yes":"Yes","confirm":"Confirm","no":"No","areyousure":"Are you sure?","closebuttontitle":"Close","unknownerror":"Unknown error"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source","select":"Select"},"block":{"addtodock":"Move this to the dock","undockitem":"Undock this item","dockblock":"Dock {$a} block","undockblock":"Undock {$a} block","undockall":"Undock all","hidedockpanel":"Hide the dock panel","hidepanel":"Hide panel"},"langconfig":{"thisdirectionvertical":"btt"},"admin":{"confirmation":"Confirmation"}};
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
var navtreeexpansions4 = [{"id":"expandable_branch_30_168055","key":"168055","type":30},{"id":"expandable_branch_30_168117","key":"168117","type":30},{"id":"expandable_branch_30_168118","key":"168118","type":30},{"id":"expandable_branch_30_168119","key":"168119","type":30},{"id":"expandable_branch_30_168120","key":"168120","type":30},{"id":"expandable_branch_30_168121","key":"168121","type":30},{"id":"expandable_branch_30_168123","key":"168123","type":30},{"id":"expandable_branch_30_168124","key":"168124","type":30},{"id":"expandable_branch_30_168125","key":"168125","type":30},{"id":"expandable_branch_30_168126","key":"168126","type":30},{"id":"expandable_branch_30_168477","key":"168477","type":30},{"id":"expandable_branch_30_168478","key":"168478","type":30},{"id":"expandable_branch_30_168479","key":"168479","type":30},{"id":"expandable_branch_0_mycourses","key":"mycourses","type":0}];
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
YUI().use('node', function(Y) {
M.util.load_flowplayer();
setTimeout("fix_column_widths()", 20);
Y.use("moodle-core-dock-loader",function() {M.core.dock.loader.initLoader();
});
 M.util.js_pending('random663bafa3b8cbe1'); Y.on('domready', function() { M.util.init_maximised_embed(Y, "presentationobject");  M.util.js_complete('random663bafa3b8cbe1'); });
Y.use("moodle-theme_essential-zoom",function() {M.theme_essential.zoom.init();
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"19","instance":"19","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"4","instance":"4","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"5","instance":"5","candock":true});
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"31230","instance":"31230","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"en"});
});
M.util.help_popups.setup(Y);
Y.use("moodle-core-popuphelp",function() {M.core.init_popuphelp();
});
M.util.init_block_hider(Y, {"id":"inst19","title":"My tasks","preference":"block19hidden","tooltipVisible":"Hide My tasks block","tooltipHidden":"Show My tasks block"});
M.util.init_block_hider(Y, {"id":"inst5","title":"Administration","preference":"block5hidden","tooltipVisible":"Hide Administration block","tooltipHidden":"Show Administration block"});
M.util.init_block_hider(Y, {"id":"inst31230","title":"Previous semester classes","preference":"block31230hidden","tooltipVisible":"Hide Previous semester classes block","tooltipHidden":"Show Previous semester classes block"});
 M.util.js_pending('random663bafa3b8cbe6'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random663bafa3b8cbe6'); });

});
//]]>
    </script>
</body>

</html>
"""

response8 = """
<!DOCTYPE html>
<html dir="ltr" lang="en" xml:lang="en" class="no-js">

<head>
    <title>CAC403-22-A-AIML: TYPES OF OS</title>
    <link rel="shortcut icon" href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/favicon" />
    <link rel="stylesheet"
        href="//mydy.dypatil.edu/rait/pluginfile.php/1/theme_essential/style/1709815567/essential.css">

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="keywords" content="moodle, CAC403-22-A-AIML: TYPES OF OS" />
    <script type="text/javascript">
        //<![CDATA[
var M = {}; M.yui = {};
M.pageloadstarttime = new Date();
M.cfg = {"wwwroot":"https:\/\/mydy.dypatil.edu\/rait","sesskey":"c5KroZlWWb","loadingicon":"https:\/\/mydy.dypatil.edu\/rait\/theme\/image.php\/essential\/core\/1709815567\/i\/loading_small","themerev":"1709815567","slasharguments":1,"theme":"essential","jsrev":"1709815567","admin":"admin","svgicons":true};var yui1ConfigFn = function(me) {if(/-skin|reset|fonts|grids|base/.test(me.name)){me.type='css';me.path=me.path.replace(/\.js/,'.css');me.path=me.path.replace(/\/yui2-skin/,'/assets/skins/sam/yui2-skin')}};
var yui2ConfigFn = function(me) {var parts=me.name.replace(/^moodle-/,'').split('-'),component=parts.shift(),module=parts[0],min='-min';if(/-(skin|core)$/.test(me.name)){parts.pop();me.type='css';min=''};if(module){var filename=parts.join('-');me.path=component+'/'+module+'/'+filename+min+'.'+me.type}else me.path=component+'/'+component+'.'+me.type};
YUI_config = {"debug":false,"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/3.17.2\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"filter":null,"insertBefore":"firstthemesheet","groups":{"yui2":{"base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/2in3\/2.9.0\/build\/","comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","combine":true,"ext":false,"root":"2in3\/2.9.0\/build\/","patterns":{"yui2-":{"group":"yui2","configFn":yui1ConfigFn}}},"moodle":{"name":"moodle","base":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?m\/1709815567\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"m\/1709815567\/","patterns":{"moodle-":{"group":"moodle","configFn":yui2ConfigFn}},"filter":null,"modules":{"moodle-core-actionmenu":{"requires":["base","event","node-event-simulate"]},"moodle-core-blocks":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification"]},"moodle-core-checknet":{"requires":["base-base","moodle-core-notification-alert","io-base"]},"moodle-core-chooserdialogue":{"requires":["base","panel","moodle-core-notification"]},"moodle-core-dock":{"requires":["base","node","event-custom","event-mouseenter","event-resize","escape","moodle-core-dock-loader"]},"moodle-core-dock-loader":{"requires":["escape"]},"moodle-core-dragdrop":{"requires":["base","node","io","dom","dd","event-key","event-focus","moodle-core-notification"]},"moodle-core-event":{"requires":["event-custom"]},"moodle-core-formautosubmit":{"requires":["base","event-key"]},"moodle-core-formchangechecker":{"requires":["base","event-focus"]},"moodle-core-handlebars":{"condition":{"trigger":"handlebars","when":"after"}},"moodle-core-lockscroll":{"requires":["plugin","base-build"]},"moodle-core-maintenancemodetimer":{"requires":["base","node"]},"moodle-core-notification":{"requires":["moodle-core-notification-dialogue","moodle-core-notification-alert","moodle-core-notification-confirm","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-core-notification-dialogue":{"requires":["base","node","panel","escape","event-key","dd-plugin","moodle-core-widget-focusafterclose","moodle-core-lockscroll"]},"moodle-core-notification-alert":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-confirm":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-exception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-notification-ajaxexception":{"requires":["moodle-core-notification-dialogue"]},"moodle-core-popuphelp":{"requires":["moodle-core-tooltip"]},"moodle-core-tooltip":{"requires":["base","node","io-base","moodle-core-notification-dialogue","json-parse","widget-position","widget-position-align","event-outside","cache-base"]},"moodle-core_availability-form":{"requires":["base","node","event","panel","moodle-core-notification-dialogue","json"]},"moodle-backup-backupselectall":{"requires":["node","event","node-event-simulate","anim"]},"moodle-backup-confirmcancel":{"requires":["node","node-event-simulate","moodle-core-notification-confirm"]},"moodle-calendar-info":{"requires":["base","node","event-mouseenter","event-key","overlay","moodle-calendar-info-skin"]},"moodle-course-categoryexpander":{"requires":["node","event-key"]},"moodle-course-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-course-coursebase","moodle-course-util"]},"moodle-course-formatchooser":{"requires":["base","node","node-event-simulate"]},"moodle-course-management":{"requires":["base","node","io-base","moodle-core-notification-exception","json-parse","dd-constrain","dd-proxy","dd-drop","dd-delegate","node-event-delegate"]},"moodle-course-modchooser":{"requires":["moodle-core-chooserdialogue","moodle-course-coursebase"]},"moodle-course-toolboxes":{"requires":["node","base","event-key","node","io","moodle-course-coursebase","moodle-course-util"]},"moodle-course-util":{"requires":["node"],"use":["moodle-course-util-base"],"submodules":{"moodle-course-util-base":{},"moodle-course-util-section":{"requires":["node","moodle-course-util-base"]},"moodle-course-util-cm":{"requires":["node","moodle-course-util-base"]}}},"moodle-form-dateselector":{"requires":["base","node","overlay","calendar"]},"moodle-form-passwordunmask":{"requires":["node","base"]},"moodle-form-shortforms":{"requires":["node","base","selector-css3","moodle-core-event"]},"moodle-form-showadvanced":{"requires":["node","base","selector-css3"]},"moodle-core_message-messenger":{"requires":["escape","handlebars","io-base","moodle-core-notification-ajaxexception","moodle-core-notification-alert","moodle-core-notification-dialogue","moodle-core-notification-exception"]},"moodle-question-chooser":{"requires":["moodle-core-chooserdialogue"]},"moodle-question-preview":{"requires":["base","dom","event-delegate","event-key","core_question_engine"]},"moodle-question-qbankmanager":{"requires":["node","selector-css3"]},"moodle-question-searchform":{"requires":["base","node"]},"moodle-availability_cohort-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_completion-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_date-form":{"requires":["base","node","event","io","moodle-core_availability-form"]},"moodle-availability_grade-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_group-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_grouping-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-availability_profile-form":{"requires":["base","node","event","moodle-core_availability-form"]},"moodle-mod_assign-history":{"requires":["node","transition"]},"moodle-mod_customcert-rearrange":{"requires":["dd-delegate","dd-drag"]},"moodle-mod_forum-subscriptiontoggle":{"requires":["base-base","io-base"]},"moodle-mod_quiz-autosave":{"requires":["base","node","event","event-valuechange","node-event-delegate","io-form"]},"moodle-mod_quiz-dragdrop":{"requires":["base","node","io","dom","dd","dd-scroll","moodle-core-dragdrop","moodle-core-notification","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-base","moodle-mod_quiz-util-page","moodle-mod_quiz-util-slot","moodle-course-util"]},"moodle-mod_quiz-modform":{"requires":["base","node","event"]},"moodle-mod_quiz-questionchooser":{"requires":["moodle-core-chooserdialogue","moodle-mod_quiz-util","querystring-parse"]},"moodle-mod_quiz-quizbase":{"requires":["base","node"]},"moodle-mod_quiz-quizquestionbank":{"requires":["base","event","node","io","io-form","yui-later","moodle-question-qbankmanager","moodle-core-notification-dialogue"]},"moodle-mod_quiz-randomquestion":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-repaginate":{"requires":["base","event","node","io","moodle-core-notification-dialogue"]},"moodle-mod_quiz-toolboxes":{"requires":["base","node","event","event-key","io","moodle-mod_quiz-quizbase","moodle-mod_quiz-util-slot","moodle-core-notification-ajaxexception"]},"moodle-mod_quiz-util":{"requires":["node"],"use":["moodle-mod_quiz-util-base"],"submodules":{"moodle-mod_quiz-util-base":{},"moodle-mod_quiz-util-slot":{"requires":["node","moodle-mod_quiz-util-base"]},"moodle-mod_quiz-util-page":{"requires":["node","moodle-mod_quiz-util-base"]}}},"moodle-message_airnotifier-toolboxes":{"requires":["base","node","io"]},"moodle-block_navigation-navigation":{"requires":["base","io-base","node","event-synthetic","event-delegate","json-parse"]},"moodle-filter_glossary-autolinker":{"requires":["base","node","io-base","json-parse","event-delegate","overlay","moodle-core-event","moodle-core-notification-alert"]},"moodle-filter_mathjaxloader-loader":{"requires":["moodle-core-event"]},"moodle-editor_atto-editor":{"requires":["node","transition","io","overlay","escape","event","event-simulate","event-custom","yui-throttle","moodle-core-notification-dialogue","moodle-core-notification-confirm","moodle-editor_atto-rangy","handlebars","timers"]},"moodle-editor_atto-plugin":{"requires":["node","base","escape","event","event-outside","handlebars","event-custom","timers"]},"moodle-editor_atto-menu":{"requires":["moodle-core-notification-dialogue","node","event","event-custom"]},"moodle-editor_atto-rangy":{"requires":[]},"moodle-format_grid-gridkeys":{"requires":["event-nav-keys"]},"moodle-report_eventlist-eventfilter":{"requires":["base","event","node","node-event-delegate","datatable","autocomplete","autocomplete-filters"]},"moodle-report_loglive-fetchlogs":{"requires":["base","event","node","io","node-event-delegate"]},"moodle-gradereport_grader-gradereporttable":{"requires":["base","node","event","handlebars","overlay","event-hover"]},"moodle-gradereport_history-userselector":{"requires":["escape","event-delegate","event-key","handlebars","io-base","json-parse","moodle-core-notification-dialogue"]},"moodle-tool_capability-search":{"requires":["base","node"]},"moodle-tool_monitor-dropdown":{"requires":["base","event","node"]},"moodle-assignfeedback_editpdf-editor":{"requires":["base","event","node","io","graphics","json","event-move","event-resize","querystring-stringify-simple","moodle-core-notification-dialog","moodle-core-notification-exception","moodle-core-notification-ajaxexception"]},"moodle-atto_accessibilitychecker-button":{"requires":["color-base","moodle-editor_atto-plugin"]},"moodle-atto_accessibilityhelper-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_align-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_bold-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_charmap-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_clear-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_collapse-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_emoticon-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_equation-button":{"requires":["moodle-editor_atto-plugin","moodle-core-event","io","event-valuechange","tabview","array-extras"]},"moodle-atto_html-button":{"requires":["moodle-editor_atto-plugin","event-valuechange"]},"moodle-atto_image-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_indent-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_italic-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_link-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_managefiles-usedfiles":{"requires":["node","escape"]},"moodle-atto_media-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_noautolink-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_orderedlist-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_rtl-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_strike-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_subscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_superscript-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_table-button":{"requires":["moodle-editor_atto-plugin","moodle-editor_atto-menu","event","event-valuechange"]},"moodle-atto_title-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_underline-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_undo-button":{"requires":["moodle-editor_atto-plugin"]},"moodle-atto_unorderedlist-button":{"requires":["moodle-editor_atto-plugin"]}}},"gallery":{"name":"gallery","base":"https:\/\/mydy.dypatil.edu\/rait\/lib\/yuilib\/gallery\/","combine":true,"comboBase":"https:\/\/mydy.dypatil.edu\/rait\/theme\/yui_combo.php?","ext":false,"root":"gallery\/1709815567\/","patterns":{"gallery-":{"group":"gallery"}}}},"modules":{"core_filepicker":{"name":"core_filepicker","fullpath":"https:\/\/mydy.dypatil.edu\/rait\/lib\/javascript.php\/1709815567\/repository\/filepicker.js","requires":["base","node","node-event-simulate","json","async-queue","io-base","io-upload-iframe","io-form","yui2-treeview","panel","cookie","datatable","datatable-sort","resize-plugin","dd-plugin","escape","moodle-core_filepicker"]},"mathjax":{"name":"mathjax","fullpath":"https:\/\/cdn.mathjax.org\/mathjax\/2.5-latest\/MathJax.js?delayStartupUntil=configured"}}};
M.yui.loader = {modules: {}};

//]]>
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js&amp;rollup/1709815567/mcore-min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/jquery-1.11.2.min.js">
    </script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/jquery.php/core/ui-1.11.4/jquery-ui.min.js">
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/bootstrap_2_3_2_min.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/jBreadCrumb_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/fitvids_1_1_1.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/theme/jquery.php/theme_essential/anti_gravity_1_1.js"></script>
    <script id="firstthemesheet" type="text/css">
        /** Required in order to fix style inclusion problems in IE with YUI **/
    </script>
    <link rel="stylesheet" type="text/css"
        href="https://mydy.dypatil.edu/rait/theme/styles.php/essential/1709815567/all" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/jquery-ui.css" />
    <link rel="stylesheet" type="text/css" href="https://mydy.dypatil.edu/rait/local/ratings/css/style.css" />
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/javascript-static.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/head">
    </script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google web fonts -->
    <!--<link href='http://fonts.googleapis.com/css?family=Domine' rel='stylesheet' type='text/css'>-->
    <!-- iOS Homescreen Icons -->

    <link rel="apple-touch-icon-precomposed" sizes="57x57"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/iphone_retina" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144"
        href="https://mydy.dypatil.edu/rait/theme/image.php/essential/theme/1709815567/homeicon/ipad_retina" />
    <!-- Start Analytics -->
    <!-- End Analytics -->

    <!--include custom fonts-->
    <style>
        @font-face {
            font-family: "Minion Pro Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/Minion-Pro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Regular";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Regular.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Light";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Light.ttf');
        }

        @font-face {
            font-family: "SourceSansPro-Semibold";
            src: url('https://mydy.dypatil.edu/rait/theme/essential/fonts/SourceSansPro-Semibold.ttf');
        }
    </style>

    <script type="text/javascript">
        $(document).ready(function() {
	  	//var $pwidth = $(window).width();
			//var $loggedin = $('body').hasClass('loggedin');

			/*if($pwidth >= 768){
				$('.offcanvas, #content-container').addClass('active');
			}*/

		  $('[data-toggle=offcanvas]').click(function() {

		  var $pwidth = $(window).width();
			$('.offcanvas').toggleClass('active');
			$('#content-container').toggleClass('active');

			//do this when in nmobile view
			var $main = $('main').hasClass('active');
			if($pwidth <= 480 ){

				if( $main == true){
					$('body, html').addClass('noscroll');
				}else{
					$('body, html').removeClass('noscroll');
				}
			}

			//do this when in tab/desktop view
			if($pwidth >= 481 ){

				//var $main = $('main').hasClass('active');

				if( $main == false){
					$('body, html').removeClass('noscroll');
				}
			}

		  });
        });
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS starts here -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-62316529-3"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag("js", new Date());
            gtag("config", "UA-62316529-3");
    </script>
    <!-- Changes by Harish(07/05/2019) for Tracking of every interaction that users perform in LMS ends here -->
</head>

<body id="page-mod-page-view"
    class="format-topcoll  path-mod path-mod-page dir-ltr lang-en yui-skin-sam yui3-skin-sam mydy-dypatil-edu--rait pagelayout-incourse course-5921 context-726963 cmid-606781 category-879 desktopdevice pagewidthnormal categoryicons zoomin two-column  has-region-side-pre used-region-side-pre has-region-footer-left empty-region-footer-left has-region-footer-middle empty-region-footer-middle has-region-footer-right empty-region-footer-right side-pre-only">

    <div class="skiplinks"><a class="skip" href="#maincontent">Skip to main content</a></div>
    <script type="text/javascript">
        //<![CDATA[
document.body.className += ' jsenabled';
//]]>
    </script>


    <header role="banner">
        <div id="page-header" class="clearfix oldnavbar">
            <div class="container-fluid">
                <div class="row-fluid">
                    <!-- HEADER: LOGO AREA -->
                    <div class="ecol12 pull-left">
                        <a class="logo" href="//mydy.dypatil.edu/rait" title="Home"></a>
                        <nav role="navigation">
                            <div class="topnavbar navbar oldnavbar moodle-has-zindex">
                                <div class="container-fluid navbar-inner">
                                    <div class="row-fluid">
                                        <div class="pull-right">
                                            <div class="usermenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a class="dropdown-toggle"
                                                            data-toggle="dropdown"
                                                            href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu pull-right">
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a>
                                                            </li>
                                                            <li class="dropdown-submenu preferences"><a
                                                                    class="dropdown-toggle" data-toggle="dropdown"
                                                                    href="#"><em><i class="fa fa-cog"></i>Preferences</em></a>
                                                                <ul class="dropdown-menu">
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a>
                                                                    </li>
                                                                    <li><a
                                                                            href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a>
                                                                    </li>
                                                                </ul>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a>
                                                            </li>
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a>
                                                            </li>
                                                            <hr class="sep" />
                                                            <li><a
                                                                    href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a>
                                                            </li>
                                                            <li><a target=""
                                                                    href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div class="messagemenu">
                                                <ul class="nav">
                                                    <li class="dropdown"><a
                                                            href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations"
                                                            class="dropdown-toggle" data-toggle="dropdown"
                                                            title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a>
                                                        <ul class="dropdown-menu">
                                                            <li><a title="You have submitted your assignment submission for Vlab - ER modeling"
                                                                    href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950">
                                                                    <div class="notification read">
                                                                        <i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span>
                                                                    </div>
                                                                </a>
                                                        </ul>
                                                </ul>
                                            </div>
                                            <div class="messagemenu messagemenu_video">
                                                <ul class="nav">
                                                    <li><a class="videotutorial"
                                                            href="https://mydy.dypatil.edu/rait/mod/page/view.php?id=101">Training
                                                            Video</a></li>
                                                </ul>
                                            </div>
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <!--<div class="messagemenu">-->
                                            <!--</div>-->
                                            <div class="gotobottommenu">
                                                <ul class="nav">
                                                    <li><a title="Go to the bottom of the page"
                                                            href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </nav>
                    </div>


                </div>
            </div>
        </div>
        <nav role="navigation">
            <div id='essentialnavbar' class="navbar oldnavbar moodle-has-zindex">
                <div class="container-fluid navbar-inner">
                    <div class="row-fluid">
                        <div class="custommenus pull-left">
                            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </a>
                            <!--<div class="pull-right">-->
                            <!--    <div class="usermenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/u/f2" alt="Picture of VIKAS CHAURASIA" title="Picture of VIKAS CHAURASIA" class="userpicture defaultuserpic" width="35" height="35" />VIKAS<i class="fa fa-caret-right"></i></a><ul class="dropdown-menu pull-right"><li><a href="https://mydy.dypatil.edu/rait/user/profile.php?id=10272"><em><i class="fa fa-user"></i>VIKAS CHAURASIA</em></a></li><li class="dropdown-submenu preferences"><a class="dropdown-toggle" data-toggle="dropdown" href="#"><em><i class="fa fa-cog"></i>Preferences</em></a><ul class="dropdown-menu"><li><a href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272&amp;returnto=profile"><em><i class="fa fa-user"></i>Edit profile</em></a></li><li><a href="https://mydy.dypatil.edu/rait/login/change_password.php"><em><i class="fa fa-key"></i>Change password</em></a></li><li><a href="https://mydy.dypatil.edu/rait/message/edit.php?id=10272"><em><i class="fa fa-comments"></i>Message preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/blog/preferences.php"><em><i class="fa fa-rss-square"></i>Blog preferences</em></a></li><li><a href="https://mydy.dypatil.edu/rait/badges/preferences.php"><em><i class="fa fa-certificate"></i>Badge preferences</em></a></li></ul></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/calendar/view.php"><em><i class="fa fa-calendar"></i>Calendar</em></a></li><li><a href="https://mydy.dypatil.edu/rait/user/files.php"><em><i class="fa fa-file"></i>Private files</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272"><em><i class="fa fa-list-alt"></i>Forum posts</em></a></li><li><a href="https://mydy.dypatil.edu/rait/mod/forum/user.php?id=10272&amp;mode=discussions"><em><i class="fa fa-list"></i>Discussions</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/badges/mybadges.php"><em><i class="fa fa-certificate"></i>Badges</em></a></li><hr class="sep" /><li><a href="https://mydy.dypatil.edu/rait/login/logout.php?sesskey=c5KroZlWWb"><em><i class="fa fa-sign-out"></i>Log out</em></a></li><li><a target="" href="mailto:lms.support@dypatil.edu?cc=getintouchwithvic@gmail.com"><em><i class="fa fa-question-circle"></i>Help</em></a></li></ul></li></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"><li class="dropdown"><a href="https://mydy.dypatil.edu/rait/message/index.php?viewing=recentconversations" class="dropdown-toggle" data-toggle="dropdown" title="Unread messages (0)"><i class="fa fa-envelope-o"></i><sup>0</sup><i class="fa fa-caret-right"></i></a><ul class="dropdown-menu"><li><a title="You have submitted your assignment submission for Vlab - ER modeling" href="https://mydy.dypatil.edu/rait/mod/assign/view.php?id=601950"><div class="notification read"><i class="fa fa-info-circle icon"></i><span class="msg-time"><i class="fa fa-comment-o"></i>6 Months ago</span><span class="notification-text">You have submitted your assignment submission for Vlab - ER modeling</span></div></a></ul></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="messagemenu">-->
                            <!--        <ul class="nav"></ul>-->
                            <!--    </div>-->
                            <!--    <div class="gotobottommenu">-->
                            <!--        <ul class="nav"><li><a title="Go to the bottom of the page" href="#region-main"><i class="fa fa-arrow-circle-o-down"></i></a></ul>-->
                            <!--    </div>-->
                            <!--</div>-->
                            <div class="nav-collapse collapse pull-left">
                                <div id="custom_menu_language">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_courses">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu">
                                    <ul class="nav"></ul>
                                </div>
                                <div id="custom_menu_activitystream">
                                </div>
                                <ul class="nav pull-left">
                                    <li class="hbl"><a href="#" class="moodlezoom"><i class="fa fa-outdent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                    <li class="sbl"><a href="#" class="moodlezoom"><i class="fa fa-indent fa-lg"></i>
                                            <span class="zoomdesc"></span></a></li>
                                </ul>

                                <!--******************code added by anil-started here*******************-->
                                <div id="custom_menu_topmenu">
                                    <!--*********code added by anil*************-->
                                    <ul class="nav">
                                        <li><a href="https://mydy.dypatil.edu/rait/" class="navbarlinks">Home</a></li>
                                        <li><a href="http://m.p-y.tm/PUPRTT" class="navbarlinks" target="_blank">Fee
                                                Payment</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php"
                                                class="navbarlinks">Exams</a></li>
                                        <li><a href="https://mydy.dypatil.edu/rait/local/dypmarket/index.php"
                                                id="marketplace">Market Place</a></li>
                                    </ul>
                                    <!--******************code added by anil-ended here*******************-->
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <div id="page" class="container-fluid">
        <div id="page-navbar" class="clearfix row-fluid">
            <div class="breadcrumb-nav pull-left">
                <ul class="breadcrumb style2">
                    <li style="z-index:99;"><a href="https://mydy.dypatil.edu/rait/my/">Dashboard</a></li>
                    <li style="z-index:98;"><a title="Operating System"
                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921">CAC403-22-A-AIML</a></li>
                    <li style="z-index:97;"><span tabindex="0">Week 1</span></li>
                    <li style="z-index:96;"><a title="Page"
                            href="https://mydy.dypatil.edu/rait/mod/page/view.php?id=606781">TYPES OF OS</a></li>
                </ul>
            </div>
            <nav class="breadcrumb-button pull-right"></nav>
        </div>
        <section role="main-content">
            <!-- Start Main Regions -->
            <div id="page-content" class="row-fluid">
                <div id="region-bs-main-and-pre" class="span12">
                    <div class="row-fluid">
                        <section id="region-main" class="span9 pull-right">
                            <h1 class="coursetitle">Operating System</h1>
                            <div class="bor"></div>
                            <div role="main"><span id="maincontent"></span>
                                <h2>TYPES OF OS</h2>
                                <div class="box generalbox center clearfix">
                                    <div class="no-overflow">
                                        <div style="padding:56.25% 0 0 0;position:relative;"><iframe
                                                src="https://player.vimeo.com/video/665900494?h=7df2fcb46a&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
                                                frameborder="0" allow="autoplay; fullscreen; picture-in-picture"
                                                allowfullscreen=""
                                                style="position:absolute;top:0;left:0;width:100%;height:100%;"
                                                title="RAIT_CE_SE-F-OS-SDB _13_01_TYPES OF os"></iframe></div>
                                        <script src="https://player.vimeo.com/api/player.js"></script>
                                    </div>
                                </div>
                                <div class="modified">Last modified: Friday, 14 January 2022, 12:31 PM</div>
                                <div id="fb-root"></div>
                                <div id="myratings"></div>
                                <div id="page_pages">
                                    <div class="like_unlike">
                                        <div id="contents_32890" style="float: left;">
                                            <div id="label_like_32890" style="float: left; padding: 0 8px 0 0;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;page&quot;, 606781, 32890, 5921, 0)" />
                                            </div>
                                            <span  id="count_likearea" class="count_likearea_32890"><a id="anchorclass_32890" href="javascript:void(0)" onClick="fnViewAllLikes(32890)">0</a></span>
                                            <div class="courselike" id="like_list_32890" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon32890"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="like_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/like.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Likes</b></span>
                                                <div class="like_32890"></div>
                                            </div>
                                            <div id="label_unlike_32890"
                                                style="float: left; padding: 0 8px 0 10px; margin-top:5px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Dislike" id="unlikeenable_image" style="cursor: pointer;" onClick="updatevalues(&quot;https://mydy.dypatil.edu/rait&quot;,&quot;page&quot;, 606781, 32890, 5921, 1)" />
                                            </div>
                                            <span id="count_unlikearea"  class="count_unlikearea_32890"><a id="anchorclass_32890" href="javascript:void(0)" onClick="fnViewAllunLikes(32890)">0</a></span>
                                            <div class="courseunlike" id="unlike_list_32890" style="display: none;">
                                                <div style="float: right; cursor: pointer;" class="closeicon32890"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="unlike_closeicon" />
                                                </div>
                                                <span><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/unlike.png" title="Like" id="likeenable_image" /></span><span >&nbsp&nbsp<b>Unlikes</b></span>
                                                <div class="unlike_32890"></div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="radiostars">
                                        <div class="overall_ratings_32890" style="float: left; cursor: pointer;"><img title='0 out of 5' src='https://mydy.dypatil.edu/rait/local/ratings/pix/star0.png'  onclick='fnViewAllRatings(5921, 606781, 32890, "page", "https://mydy.dypatil.edu/rait", "TYPES OF OS")'/>
                                        </div>
                                        <div class="overall_users">(<font class='totalcount_32890'>0</font> users)</div>
                                    </div>
                                    <div class="mycomment"><a id="anchorclass_32890" href="javascript:void(0)"
                                            onClick="fnViewAllComments(32890)"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/comment.png" title="Comment" id="custom_icons" /></a>&nbsp;(
                                        <font class="commentcount_32890">0</font>)<div class="coursecomment"
                                            id="comment_list_32890" style="display: none;">
                                            <div style="float: right; cursor: pointer;" class="closeicon32890"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/icon_close_popup.gif" title="Close" id="comment_closeicon" />
                                            </div>
                                            <textarea name="commentarea" id="mycomment_32890" rows="2" cols="50"></textarea><a
                                                class="commentclick_32890" href="javascript:void(0)"
                                                onClick="fnComment(5921, 606781, 32890, &quot;page&quot;, &quot;https://mydy.dypatil.edu/rait&quot;)"
                                                style="font-size: 12px;"><img src="https://mydy.dypatil.edu/rait/local/ratings/pix/add-comment.gif" /></a>
                                            <div class="comment_32890"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <aside id="block-region-side-pre" class="span3 desktop-first-column block-region"
                            data-blockregion="side-pre" data-droptarget="1"><a href="#sb-1" class="skip-block">Skip My
                                tasks</a>
                            <div id="inst19" class="block_universitystructure  block" role="complementary"
                                data-block="universitystructure" data-instanceid="19"
                                aria-labelledby="instance-19-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-19-header">My tasks</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Learnings</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/timetable/calendarview.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">TimeTable Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/myacademics/transcript.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Transcript</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/academiccalendar"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Academic Calendar</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/feemanagement/studentfeedetails.php"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Fee Details</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        <li class="type_category depth_3 contains_branch">
                                            <p class="tree_item branch active_tree_node">
                                                <span class="usdimmed_text" >Examination</span>
                                            <ul>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/scheduledexams.php">Scheduled
                                                            Exams</a></p>
                                                </li>
                                                <li class="type_course depth_4 collapsed contains_branch">
                                                    <p class="tree_item nomodule hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/examination/studentresults.php">Student
                                                            Examsresults </a></p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_3 contains_branch">
                                            <p class="tree_item branch hasicon active_tree_node">
                                                <span class="usdimmed_text" >My Profile</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/profile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">View Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/profilechange/changeprofile.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Edit Profile</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/local/users/change_password.php?id=10272"><img  id= "us1_block_branchicon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Change Password</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-1" class="skip-block-to"></span><a href="#sb-3" class="skip-block">Skip
                                Administration</a>
                            <div id="inst5" class="block_settings  block" role="navigation" data-block="settings"
                                data-instanceid="5" aria-labelledby="instance-5-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-5-header">Administration</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <div id="settingsnav" class="box block_tree_box">
                                        <ul class="block_tree list">
                                            <li class="type_course collapsed contains_branch" aria-expanded="false">
                                                <p class="tree_item branch root_node">
                                                    <span tabindex="0">Course administration</span></p>
                                                <ul>
                                                    <li class="type_setting collapsed item_with_icon">
                                                        <p class="tree_item leaf"><a
                                                                href="https://mydy.dypatil.edu/rait/grade/report/index.php?id=5921"><i class="fa fa-table icon" title=""><img alt="" class="smallicon navicon" title="" src="https://mydy.dypatil.edu/rait/theme/image.php/essential/core/1709815567/i/grades" /></i>Grades</a>
                                                        </p>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div><span id="sb-3" class="skip-block-to"></span><a href="#sb-5" class="skip-block">Skip
                                Previous semester classes</a>
                            <div id="inst31230" class="block_stu_previousclasses  block" role="complementary"
                                data-block="stu_previousclasses" data-instanceid="31230"
                                aria-labelledby="instance-31230-header" data-dockable="1">
                                <div class="header">
                                    <div class="title">
                                        <div class="block_action"></div>
                                        <h2 id="instance-31230-header">Previous semester classes</h2>
                                    </div>
                                </div>
                                <div class="content">
                                    <ul class="block_tree list">
                                        <li class="type_unknown depth_1 contains_branch simple_invisible">
                                            <p class="tree_item branch active_tree_node navigation_node">
                                                <span  ><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png"></span>
                                        <li class="type_course depth_2 contains_branch">
                                            <p class="tree_item branch hasiconactive_tree_node">
                                                <span class="usdimmed_text" >Semester I</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4642"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics I</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4643"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Structered Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4644"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Electronics Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4645"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Physics</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=4646"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">English For Engineers</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester II</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5067"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Mathematics-II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5068"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Engineering Chemistry II</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5069"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Data Structures</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5071"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Digital Logic Design</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5072"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Environmental Studies</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5070"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Principles of Communication Engineering</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester III</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5197"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Database Management System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5198"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Design and Analysis of Algorithms</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5199"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Object Oriented Programming</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5200"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Computer Organization & Architecture</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5201"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Statistical Methods</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                        <li class="type_course depth_2 collapsed contains_branch">
                                            <p class="tree_item branch hasicon">
                                                <span class="usdimmed_text" >Semester IV</span>
                                            <ul>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5919"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Artificial Intelligence</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5920"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Software Engineering</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5921"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Operating System</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5922"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Programming with Python</a>
                                                    </p>
                                                </li>
                                                <li class="contains_branch item_with_icon">
                                                    <p class="tree_item leaf hasicon"><a
                                                            href="https://mydy.dypatil.edu/rait/course/view.php?id=5923"
                                                            target="_blank"><img  id= "us1_block_branchiMycon"  class="smallicon navicon" src="https://mydy.dypatil.edu/rait/pix/i/navigationitem.png">Formal Language Automata Language</a>
                                                    </p>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                    </li>
                                    </ul>
                                </div>
                            </div><span id="sb-5" class="skip-block-to"></span>
                        </aside>
                    </div>
                </div>
            </div>
            <!-- End Main Regions -->
        </section>
    </div>

    <footer role="contentinfo" id="page-footer">
        <div class="container-fluid">
            <div class="row-fluid footerblocks">
                <div class="span8 pull-left footersite-text">
                    <p>
                    <h4>'Education is not the learning of many facts </h4>
                    </p>
                    <p>
                    <h4>but the training of the mind to think.' - Albert Einstein</h4>
                    </p>
                </div>
                <div class="span4 pull-right footersite-icons">
                </div>
            </div>
            <div class="row-fluid footerblocks">
                <div class="span4 pull-left">
                    <div class="column">
                        <aside id="block-region-footer-left" class="block-region" data-blockregion="footer-left"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 center">
                    <div class="column">
                        <aside id="block-region-footer-middle" class="block-region" data-blockregion="footer-middle"
                            data-droptarget="1"></aside>
                    </div>
                </div>
                <div class="span4 pull-right">
                    <div class="column">
                        <aside id="block-region-footer-right" class="block-region" data-blockregion="footer-right"
                            data-droptarget="1"></aside>
                    </div>
                </div>
            </div>
            <div class="footerlinks row-fluid">
                <hr />
                <span class="helplink"></span>
            </div>
            <div class="footerperformance row-fluid">
            </div>
            <div class="footercredit row-fluid">
                The Essential theme is developed, enhanced and maintained by <a href="//about.me/gjbarnard"
                    target="_blank">Gareth J Barnard</a>
            </div>
        </div>
    </footer>
    <a href="#top" class="back-to-top"><i class="fa fa-angle-up "></i></a>
    <!--js file commented and included in blocks/events instead of adding in theme footer-->
    <!--<script src="https://cdn.rawgit.com/vast-engineering/jquery-popup-overlay/1.7.10/jquery.popupoverlay.js"></script>-->
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/custom_zoom.js"></script>
    <script src="https://mydy.dypatil.edu/rait/theme/essential/jquery/select2.min.js"></script>
    <link href="https://mydy.dypatil.edu/rait/theme/essential/style/select2.min.css" rel="stylesheet" />

    <script type="text/javascript">
        jQuery(document).ready(function () {
            $('#id_cobaltcourseid').select2();
            $('#id_onlinecourseid').select2();
            jQuery('#essentialnavbar').affix({offset: {top: $('#page-header').height()}});$('#page').fitVids();        });
    </script>
    <script type="text/javascript">
        //<![CDATA[
var require = {
    baseUrl : 'https://mydy.dypatil.edu/rait/lib/requirejs.php/1709815567/',
    // We only support AMD modules with an explicit define() statement.
    enforceDefine: true,
    skipDataMain: true,

    paths: {
        jquery: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/jquery-1.11.2.min',
        jqueryui: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/jquery/ui-1.11.4/jquery-ui.min',
        jqueryprivate: 'https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/jquery-private'
    },

    // Custom jquery config map.
    map: {
      // '*' means all modules will get 'jqueryprivate'
      // for their 'jquery' dependency.
      '*': { jquery: 'jqueryprivate' },

      // 'jquery-private' wants the real jQuery module
      // though. If this line was not here, there would
      // be an unresolvable cyclic dependency.
      jqueryprivate: { jquery: 'jquery' }
    }
};

//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/lib/requirejs/require.min.js"></script>
    <script type="text/javascript">
        //<![CDATA[
require(['core/first'], function() {
;
require(["core/log"], function(amd) { amd.setConfig({"level":"warn"}); });
});
//]]>
    </script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/ratings.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/facebook.js"></script>
    <script type="text/javascript"
        src="https://mydy.dypatil.edu/rait/lib/javascript.php/1709815567/local/ratings/js/twitter.js"></script>
    <script type="text/javascript" src="https://mydy.dypatil.edu/rait/theme/javascript.php/essential/1709815567/footer">
    </script>
    <script type="text/javascript">
        //<![CDATA[
M.str = {"moodle":{"lastmodified":"Last modified","name":"Name","error":"Error","info":"Information","viewallcourses":"View all courses","morehelp":"More help","loadinghelp":"Loading...","cancel":"Cancel","yes":"Yes","confirm":"Confirm","no":"No","areyousure":"Are you sure?","closebuttontitle":"Close","unknownerror":"Unknown error"},"repository":{"type":"Type","size":"Size","invalidjson":"Invalid JSON string","nofilesattached":"No files attached","filepicker":"File picker","logout":"Logout","nofilesavailable":"No files available","norepositoriesavailable":"Sorry, none of your current repositories can return files in the required format.","fileexistsdialogheader":"File exists","fileexistsdialog_editor":"A file with that name has already been attached to the text you are editing.","fileexistsdialog_filemanager":"A file with that name has already been attached","renameto":"Rename to \"{$a}\"","referencesexist":"There are {$a} alias\/shortcut files that use this file as their source","select":"Select"},"block":{"addtodock":"Move this to the dock","undockitem":"Undock this item","dockblock":"Dock {$a} block","undockblock":"Undock {$a} block","undockall":"Undock all","hidedockpanel":"Hide the dock panel","hidepanel":"Hide panel"},"langconfig":{"thisdirectionvertical":"btt"},"admin":{"confirmation":"Confirmation"}};
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
var navtreeexpansions4 = [{"id":"expandable_branch_30_168055","key":"168055","type":30},{"id":"expandable_branch_30_168118","key":"168118","type":30},{"id":"expandable_branch_30_168119","key":"168119","type":30},{"id":"expandable_branch_30_168120","key":"168120","type":30},{"id":"expandable_branch_30_168121","key":"168121","type":30},{"id":"expandable_branch_30_168122","key":"168122","type":30},{"id":"expandable_branch_30_168123","key":"168123","type":30},{"id":"expandable_branch_30_168124","key":"168124","type":30},{"id":"expandable_branch_30_168125","key":"168125","type":30},{"id":"expandable_branch_30_168126","key":"168126","type":30},{"id":"expandable_branch_30_168477","key":"168477","type":30},{"id":"expandable_branch_30_168478","key":"168478","type":30},{"id":"expandable_branch_30_168479","key":"168479","type":30},{"id":"expandable_branch_0_mycourses","key":"mycourses","type":0}];
//]]>
    </script>
    <script type="text/javascript">
        //<![CDATA[
YUI().use('node', function(Y) {
M.util.load_flowplayer();
setTimeout("fix_column_widths()", 20);
Y.use("moodle-core-dock-loader",function() {M.core.dock.loader.initLoader();
});
Y.use("moodle-theme_essential-zoom",function() {M.theme_essential.zoom.init();
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"19","instance":"19","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"4","instance":"4","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"5","instance":"5","candock":true});
});
Y.use("core_dock","moodle-block_navigation-navigation",function() {M.block_navigation.init_add_tree({"id":"31230","instance":"31230","candock":true,"courselimit":"20","expansionlimit":0});
});
Y.use("moodle-filter_mathjaxloader-loader",function() {M.filter_mathjaxloader.configure({"mathjaxconfig":"\nMathJax.Hub.Config({\n    config: [\"Accessible.js\", \"Safe.js\"],\n    errorSettings: { message: [\"!\"] },\n    skipStartupTypeset: true,\n    messageStyle: \"none\"\n});\n","lang":"en"});
});
M.util.help_popups.setup(Y);
Y.use("moodle-core-popuphelp",function() {M.core.init_popuphelp();
});
M.util.init_block_hider(Y, {"id":"inst19","title":"My tasks","preference":"block19hidden","tooltipVisible":"Hide My tasks block","tooltipHidden":"Show My tasks block"});
M.util.init_block_hider(Y, {"id":"inst5","title":"Administration","preference":"block5hidden","tooltipVisible":"Hide Administration block","tooltipHidden":"Show Administration block"});
M.util.init_block_hider(Y, {"id":"inst31230","title":"Previous semester classes","preference":"block31230hidden","tooltipVisible":"Hide Previous semester classes block","tooltipHidden":"Show Previous semester classes block"});
 M.util.js_pending('random663bb070d5c655'); Y.on('domready', function() { M.util.js_complete("init");  M.util.js_complete('random663bb070d5c655'); });

});
//]]>
    </script>
</body>

</html>
"""


soup = BeautifulSoup(response2, 'lxml')

#CASE I (successfully extracted)

# !!! https://mydy.dypatil.edu/rait/mod/page/view.php?id=606787 !!!
# the above links seems to defy this parsing method, although this type of file is rarely uploaded, or even accessed. 
# considering dropping support for this link instead.

#extracting the URL for the pdf from response1 type of page
presentation_content = soup.find('div', attrs={'role':'main'})

soup = BeautifulSoup(str(presentation_content), 'lxml')
link_to_content = soup.find("a")
link_to_content = link_to_content['href']
print("FIRST: ",link_to_content) #success


print("SECONND___________________________")
#CASE II (successfully done | although I want to do more testing on other links to ensure it's robustness) 
#extracting url from flexpaper type of page (response2)
import re
soup = BeautifulSoup(response2, 'lxml')

#find the script that handles "displaying the pdf file within the custom (flexpaper) pdf viewer"
script_tag = soup.find('script', string=re.compile(r"\$\(.*?\).FlexPaperViewer"))
if script_tag != None:
    #Extract the PDFFILE link from within its config by means of regex
    pdf_url_pattern = re.compile(r"PDFFile\s*:\s*'([^']+)'")

    pdf_url_match = pdf_url_pattern.search(script_tag.string)

    if(pdf_url_match):
        #successfully found the PDFFILE url
        pdf_url = pdf_url_match.group(1)
        print("PDF file URL:", pdf_url)
        # print(pdf_url_match)
        
    else:
        ... #not found to be considered









