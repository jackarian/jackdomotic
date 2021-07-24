/**
 * 
 */
var base_url = 'http://0.0.0.0:8080/ssc/api'

var list_plc = base_url + '/plc';
var add_plc = base_url + '/plc';
var invio_comando = base_url+"/resource/command";

var reservations= base_url+"/resource/reservation";
var inserisci_prenotazione= base_url+"/resource/attiva-prenotazione";
var sospensione    = base_url+"/resource/scheduler/suspend_job";
var terminazione   = base_url+"/resource/scheduler/terminate_job";
var riattivazione  = base_url+"/resource/scheduler/resume_job";