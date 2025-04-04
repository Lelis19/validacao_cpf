import pytest
from app.validacao import validar_cpf

# Testa CPFs válidos conhecidos
def test_cpf_valido():
    assert validar_cpf("380.561.540-00")
    assert validar_cpf("67746487033")

# Testa CPFs com dígitos verificadores incorretos
def test_cpf_invalido():
    assert not validar_cpf("357.159.258-23")
    assert not validar_cpf("95135785211")

# Testa CPFs com caracteres inválidos
def test_cpf_caracteres_invalidos():
    assert not validar_cpf("3a7.1b9.2c8-gh")
    assert not validar_cpf("9#1s5@8f2$1")

# Testa CPFs com quantidade errada de dígitos
def test_cpf_comprimento_invalido():
    assert not validar_cpf("357.1595.2584-23")
    assert not validar_cpf("185211")
    assert not validar_cpf("")

# Testa CPFs compostos por números repetidos
def test_cpf_numeros_iguais():
    assert not validar_cpf("111.111.111-11")
    assert not validar_cpf("22222222222")
